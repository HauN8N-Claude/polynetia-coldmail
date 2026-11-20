# Stratégie coldmail PolynetIA

Documents de travail pour reprendre la stratégie d’acquisition de PolynetIA sur un autre ordinateur. État de référence : 20 novembre 2026.

**Commencer par [l’état actuel et l’ordre de reprise](16_Etat_actuel_et_reprise.md), puis lire [AGENTS.md](AGENTS.md). Les deux campagnes Instantly existantes restent en brouillon ; le fondateur garde le lancement manuel.**

## Documents principaux

| Besoin | Document |
| --- | --- |
| Reprendre le travail et connaître les validations | [État actuel](16_Etat_actuel_et_reprise.md) |
| Écrire objets, mails et PS | [Guide de rédaction dédié](15_Guide_redaction_objets_mails_PS.md) |
| Appliquer les règles communes | [Règles coldmail](11_Regles_redaction_coldmail.md) |
| Adapter le langage à un artisan | [Référentiel artisans](12_ICP_Artisans.md) |
| Adapter le langage à un dirigeant | [Référentiel dirigeants](13_ICP_Dirigeants.md) |
| Relire les copies enregistrées dans les deux brouillons | [CF04 et CF17](14_Brouillons_Instantly_CF04_CF17.md) |
| Retrouver les modèles textuels du mentor | [Bibliothèque de templates](07_Templates_emails_du_mentor.md) |
| Comprendre le système complet | [Système d’acquisition](02_Systeme_acquisition_agence_V01.md) |
| Retrouver une décision et son origine | [Registre](04_Registre_sources_et_decisions.md) |
| Comprendre variables, délais et boîtes | [Paramétrage Instantly](10_Parametrage_Instantly.md) |
| Retrouver les volumes par métier | [Segmentation](Segmentation_Instantly.md) |

## Ce qui est public

La stratégie, les transcriptions textuelles fournies comme ressources, les modèles, les recommandations, les adaptations, les règles et les états de validation. Les sources du mentor restent distinguées des propositions de PolynetIA ; aucun statut « testé » n’est attribué à nos nouvelles variantes sans résultat.

Les CSV de leads, coordonnées individuelles, exports API, adresses d’envoi, identifiants internes et clés d’accès restent privés. Les mentions `[adresse privée]` et `[identifiant privé]` signalent une donnée retirée de cette copie publique. Les documents originaux PDF, Word, images et les pièces du cas client, de l’étude et de la vidéo ne sont pas stockés ici.

## Reprendre sur un autre PC

Suivre [REPRISE_AUTRE_PC.md](REPRISE_AUTRE_PC.md). La clé Instantly se configure localement sous `INSTANTLY_API_KEY` ; `.env.example` contient uniquement le nom de la variable. Retrouver les brouillons par leurs noms via une lecture API avant toute modification ; ne pas recréer les campagnes parce que leurs identifiants sont absents de ce dépôt public.

## Publier une mise à jour

Modifier les documents, consigner les validations, puis lancer `python scripts/check_publication.py`. Examiner les fichiers sélectionnés avant un commit et un push. La liste des fichiers admis est limitée dans `.gitignore` ; ajouter explicitement un nouveau document après contrôle. Ne jamais importer des données privées dans l’historique Git.
