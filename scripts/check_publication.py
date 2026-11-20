"""Check public documentation before commit. Does not make network calls."""
from pathlib import Path
import os
import re
import subprocess
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
required = ['AGENTS.md', 'README.md', 'REPRISE_AUTRE_PC.md', '11_Regles_redaction_coldmail.md',
            '15_Guide_redaction_objets_mails_PS.md', '16_Etat_actuel_et_reprise.md']
problems = []
for name in required:
    if not (ROOT / name).is_file():
        problems.append('Missing document: ' + name)
patterns = {
    'credential': r'(?i)(?:gh[pousr]_[A-Za-z0-9_]{15,}|github_pat_[A-Za-z0-9_]{15,}|sk-[A-Za-z0-9_-]{20,}|bearer\s+[A-Za-z0-9_-]{15,})',
    'private_uuid': r'\b[0-9a-fA-F]{8}-(?:[0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}\b',
    'email_address': r'\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b',
    'absolute_windows_path': r'[A-Z]:[/\\]Users[/\\]',
}
result = subprocess.run(['git', 'ls-files', '--cached', '-z'], cwd=ROOT, capture_output=True)
names = result.stdout.decode('utf-8').split('\0') if result.returncode == 0 else []
files = [ROOT / n for n in names if n] or [p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts]
for path in files:
    relative = path.relative_to(ROOT).as_posix()
    allowed = path.suffix in ('.md', '.py') or path.name in ('.gitignore', '.gitattributes', '.env.example')
    if not allowed or any(part in ('Leads_Instantly', 'tmp', '.preparation_instantly') for part in path.parts):
        problems.append('Disallowed public file: ' + relative)
        continue
    text = path.read_text(encoding='utf-8')
    for variable in ('INSTANTLY_API_KEY', 'GH_TOKEN', 'GITHUB_TOKEN'):
        value = os.environ.get(variable, '')
        if value and value in text:
            problems.append('Configured secret found: ' + relative)
    for label, pattern in patterns.items():
        if re.search(pattern, text):
            problems.append(label + ': ' + relative)
    if path.suffix == '.md':
        for match in re.finditer(r'\[[^\]\n]+\]\((<?[^)\n]+>?)\)', text):
            target = unquote(match.group(1).strip('<>')).split('#')[0]
            if not target or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                continue
            if not (path.parent / target).exists():
                problems.append('Broken local link: ' + relative + ' -> ' + target)
if problems:
    print('PUBLICATION BLOCKED')
    print('\n'.join(problems))
    raise SystemExit(1)
print('PUBLICATION CHECK PASSED: ' + str(len(files)) + ' files; no private pattern or broken local link detected.')
