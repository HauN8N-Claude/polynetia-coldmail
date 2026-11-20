# Segmentation des leads Instantly

Règle de rédaction actualisée du 19 novembre 2026 : CF04 et CF17 sont retenus dans la bibliothèque 07. Les nouvelles campagnes Cimetière et Salaire fantôme utilisent le Word fourni et leurs copies sont dans la fiche 09 révisée. Claude prépare leurs listes ; les volumes et fichiers historiques décrits ci-dessous ne leur sont pas attribués automatiquement. Les premiers essais libres restent historiques.

Mise à jour d’orientation du 19 novembre 2026 : les fichiers et chiffres ci-dessous décrivent la préparation du 17 novembre. Pour le pilote actuellement demandé, consulter `05_Premiere_campagne_PolynetIA.md` : un seul lot de cinquante contacts PV_0-5 réparti entre dix copies exploratoires. Les trois approches suivantes sont préparées dans le document 09, sans chevauchement de contacts. Les recommandations de lancement simultané des quatre segments ci-dessous sont historiques.

Préparation du 17 novembre 2026. Source : QUALITENR_INSTANTLY_IMPORT.csv, 10 950 leads et 17 colonnes.

## Proposition retenue

Neuf segments pour démarrer. L'activité permet d'adapter le message au métier et de conserver un ServiceHook cohérent. Pour les trois activités les plus représentées (PAC, PV, BOIS), deux groupes de taille permettent de tester des angles différents : 0 à 5 salariés et 6 à 19 salariés, d'après les classes TeamSize du fichier. Les effectifs sont repris de la source et n'ont pas été revérifiés. Les trois activités moins représentées restent chacune en un seul segment pour garder du volume.

L'offre précisée le 17 novembre 2026 couvre quatre mécanismes : acquisition publicitaire locale pour des projets photovoltaïques, PAC et climatisation, qualification des demandes selon les critères de l'installateur, parcours de prise de rendez-vous, puis suivi et relances commerciales. Les résultats chiffrés, conditions commerciales et garanties restent à préciser avant rédaction finale.

Pour cette offre, les quatre segments PAC_0-5, PAC_6-19, PV_0-5 et PV_6-19 constituent le premier périmètre de prospection : 9 075 leads et 184 fichiers de lots. BOIS, VENTILATION, SOLAIRE et AUTRE restent en réserve : 1 875 leads et 41 fichiers. Leur activité principale ne prouve pas l'absence d'une activité secondaire PAC, photovoltaïque ou climatisation ; cette activité doit être confirmée avant de les intégrer à ces campagnes. SOLAIRE désigne le solaire thermique et ne doit pas être assimilé au photovoltaïque. Aucun segment climatisation n'est identifié dans le fichier actuel.

Hypothèses d'angles à tester : pour les structures de 0 à 5 salariés, des demandes correspondant à leur zone et prestations, avec moins de temps consacré au tri et aux rappels ; pour celles de 6 à 19 salariés, la régularité des opportunités, la qualification avant rendez-vous et l'organisation du suivi commercial. La taille ne démontre pas qu'une entreprise rencontre ces difficultés : les messages les présenteront comme des questions ou des possibilités, jamais comme des constats non vérifiés.

| Segment de campagne | Leads | Lots de 50 | Dernier lot partiel |
| --- | ---: | ---: | ---: |
| PAC_0-5 | 4708 | 94 | 8 |
| PAC_6-19 | 1962 | 39 | 12 |
| PV_0-5 | 1467 | 29 | 17 |
| PV_6-19 | 938 | 18 | 38 |
| BOIS_0-5 | 1022 | 20 | 22 |
| BOIS_6-19 | 532 | 10 | 32 |
| VENTILATION | 155 | 3 | 5 |
| SOLAIRE | 56 | 1 | 6 |
| AUTRE | 110 | 2 | 10 |

Total : 10950 leads dans 225 fichiers, dont 216 lots de 50 et 9 lots partiels. Tous les leads sont conservés une seule fois parmi les lots. Les reliquats restent dans leur segment.

## Utilisation

- Le dossier Leads_Instantly contient uniquement le fichier principal et les CSV de leads, rangés en sous-dossiers. L'index et ce guide sont placés à côté.
- Le master est une copie exacte de la source. Importer les lots ou le master : ne pas les importer ensemble. Utiliser les lots pour conserver la segmentation.
- Préparer d'abord une campagne pour chacun des quatre segments PAC/PV retenus, sous réserve de validation des textes. Les lots successifs d'un même segment peuvent alimenter cette même campagne : un lot de 50 ne nécessite pas une nouvelle campagne. Les cinq autres segments restent en réserve.
- Commencer par un lot de 50 par segment ciblé. Si l'offre vise une seule activité, commencer uniquement par cette activité. Comparer les réponses positives et les rendez-vous rapportés aux leads contactés. Cinquante leads donnent un premier signal, à confirmer sur les lots suivants.
- Les leads sont mélangés de façon reproductible dans chaque segment pour éviter de reprendre l'ordre du fichier source. Les lots ne sont pas des quotas géographiques et ne garantissent pas des proportions exactement identiques de types de boîte mail.
- La géographie, les classes TeamSize détaillées et MailboxType restent disponibles dans chaque CSV. Pas de sous-campagne par département à ce stade : les volumes seraient trop dispersés, sauf besoin commercial local précis.

## Import et personnalisation

Les 17 colonnes originales et toutes leurs valeurs sont conservées, sans prénom ni fonction ajoutés. Les CSV de lots sont en UTF-8 avec BOM, séparés par virgules, avec une ligne d'en-têtes en plus des leads. Les téléphones, SIRET et départements restent des chaînes de caractères pour conserver les zéros initiaux.

Mapper Email vers le champ Email, FirstName vers First Name, LastName vers Last Name et CompanyName vers Company Name. Conserver notamment Greeting, Activity, ServiceHook, TeamSize, Segment et MailboxType en variables personnalisées si utilisées dans les messages. Vérifier les correspondances proposées lors de l'import.

Le contrôle du 19 novembre confirme le même schéma de 17 colonnes dans les 225 lots. Le mapping détaillé, le traitement des champs vides et les vérifications avant envoi sont centralisés dans `10_Parametrage_Instantly.md`. Les copies actuelles utilisent « Bonjour, » et n’imposent aucune variable de prénom.

Le fichier distingue 3 027 boîtes génériques, 6 272 identités non confirmées et 1 651 noms de dirigeant probables. Un nom probable reste une hypothèse de la source. Pour le premier test, privilégier « Bonjour, » dans le message tant que l'identité n'a pas été confirmée. Les Greeting originaux restent conservés dans les CSV.

Aucun doublon d'email ni de SIRET n'a été trouvé. Le contrôle de forme des emails ne vérifie pas leur existence ni leur délivrabilité. La vérification des emails et les exclusions des contacts déjà sollicités restent à effectuer dans Instantly avant l'envoi. Aucune campagne n'a été créée ni lancée.

Documentation : [Importer un CSV et mapper les variables](https://help.instantly.ai/en/articles/6254215-how-to-add-leads-to-your-campaign-from-a-csv-file), [Gérer les doublons](https://help.instantly.ai/en/articles/7891047-check-for-duplicate-leads), [Vérifier les emails](https://help.instantly.ai/en/articles/6514690-how-to-verify-leads).
