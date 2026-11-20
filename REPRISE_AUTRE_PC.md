# Reprendre le travail sur un autre ordinateur

## 1. Récupérer les documents

Avec Git installé :

```sh
git clone https://github.com/HauN8N-Claude/polynetia-coldmail.git
cd polynetia-coldmail
```

Il est également possible de télécharger le ZIP depuis GitHub pour une lecture simple. Pour modifier et synchroniser le travail, préférer le clone Git et connecter GitHub avec son propre compte.

## 2. Donner le contexte à l’assistant

Ouvrir ce dossier comme espace de travail et utiliser cette consigne :

> Lis AGENTS.md, 16_Etat_actuel_et_reprise.md, 15_Guide_redaction_objets_mails_PS.md et 11_Regles_redaction_coldmail.md. Reprends la stratégie coldmail PolynetIA à partir des dernières validations. CF04 et CF17 existent déjà dans Instantly en brouillon : retrouve-les par lecture API, ne les recrée pas et ne les active pas. Le travail en cours porte sur le choix des objets, puis la validation des copies et des lexiques.

Les modèles d’origine, propositions et textes enregistrés sont distincts. L’état actuel prime sur les anciennes mentions « en attente » dans les historiques.

## 3. Rétablir l’accès privé à Instantly

Fournir la clé dans la variable d’environnement locale `INSTANTLY_API_KEY`, avec le mécanisme de secrets de l’environnement utilisé. La clé n’est ni présente ni récupérable dans ce dépôt. `.env.example` est un exemple vide ; il ne charge pas automatiquement une variable dans un outil.

Effectuer d’abord une lecture des campagnes du compte et rechercher les noms CF04 et CF17 indiqués dans l’état actuel. Vérifier leur statut réel, leurs leads et leurs copies, car le compte peut avoir changé depuis l’état de référence. Les identifiants internes seront retrouvés dans la réponse API ; ne pas les ajouter au dépôt public.

Les CSV de leads et les pièces des ressources promises, s’ils sont nécessaires, doivent être transférés séparément par un canal privé. Ne pas les ajouter au dépôt public. Les dossiers `Leads_Instantly`, `tmp` et `.preparation_instantly` du PC d’origine n’y figurent pas.

## 4. Garder les versions synchronisées

Avant de commencer sur un PC, faire `git pull --ff-only`. Après modification et contrôle, créer un commit avec les seuls fichiers de stratégie concernés, puis pousser la branche. Ne pas travailler simultanément sur le même document depuis deux PC sans synchronisation.

Avant un push, lancer :

```sh
python scripts/check_publication.py
git diff --check
git status --short
```

Le contrôle vérifie la présence des documents essentiels, les liens Markdown locaux et des motifs de données privées dans les fichiers destinés à Git. Un nouveau type de fichier doit être examiné avant d’être ajouté à la liste autorisée.
