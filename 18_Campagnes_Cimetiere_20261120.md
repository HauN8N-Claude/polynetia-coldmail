# Campagnes Cimetière préparées le 20 novembre 2026

**Huit campagnes ont été créées par API, une par fichier fourni, et restent en brouillon. Aucun envoi test ni appel d’activation n’a été effectué. Les statuts des anciennes campagnes ont été conservés lors de la relecture.**

Le dossier source contient 183 lignes. Deux lignes partagent la même adresse email entre des entreprises différentes : elles sont conservées à part pour vérification. Huit autres contacts existent déjà dans le workspace et ont été écartés par skip_if_in_workspace. Au total, 173 contacts ont été importés.

## Répartition par fichier

| Segment du fichier | Lignes source | Importés | Déjà présents | Adresse partagée en attente |
| --- | ---: | ---: | ---: | ---: |
| RENO_DIRIGEANT_part1 | 50 | 48 | 1 | 1 |
| RENO_DIRIGEANT_part2 | 50 | 49 | 0 | 1 |
| RENO_DIRIGEANT_part3 | 25 | 25 | 0 | 0 |
| RENO_ARTISAN | 28 | 27 | 1 | 0 |
| PAC_DIRIGEANT | 11 | 7 | 4 | 0 |
| PAC_ARTISAN | 8 | 8 | 0 | 0 |
| SOLAIRE_DIRIGEANT | 7 | 5 | 2 | 0 |
| SOLAIRE_ARTISAN | 4 | 4 | 0 | 0 |
| **Total** | **183** | **173** | **8** | **2** |

Les sources sont inchangées. Les lignes mises en attente sont repérées dans le registre privé (fichier privé à transférer séparément). Leur adresse commune n’a pas été arbitrairement rattachée à l’une des deux sociétés.

## Noms à rechercher dans Instantly

- `[A VALIDER] CIMETIERE | RENO_DIRIGEANT_part1 | FRAIS90J 2026-11-20`
- `[A VALIDER] CIMETIERE | RENO_DIRIGEANT_part2 | FRAIS90J 2026-11-20`
- `[A VALIDER] CIMETIERE | RENO_DIRIGEANT_part3 | FRAIS90J 2026-11-20`
- `[A VALIDER] CIMETIERE | RENO_ARTISAN | FRAIS90J 2026-11-20`
- `[A VALIDER] CIMETIERE | PAC_DIRIGEANT | FRAIS90J 2026-11-20`
- `[A VALIDER] CIMETIERE | PAC_ARTISAN | FRAIS90J 2026-11-20`
- `[A VALIDER] CIMETIERE | SOLAIRE_DIRIGEANT | FRAIS90J 2026-11-20`
- `[A VALIDER] CIMETIERE | SOLAIRE_ARTISAN | FRAIS90J 2026-11-20`

## Séquence retenue

Le fondateur a choisi de préparer trois mails et de garder en attente la relance fondée sur une observation du parcours. Les CSV ne contiennent pas cette observation.

1. Premier contact à J0 : historique publicitaire et proposition du rapport d’une page.
2. Relance 1, trois jours après : volume des demandes ou transformation commerciale.
3. Dernier suivi, quatre jours après la relance 1 : clôture et possibilité de recevoir la fiche.

**La relance « Le point que j’ai relevé… » n’est pas dans les séquences automatiques.** Elle pourra être ajoutée après collecte d’une observation réelle et vérifiée. Aucun observedFunnelSignal générique n’a été inventé ou importé.

Les dernières publicités archivées sont datées dans les fichiers ; cela ne permet pas de déduire un échec commercial ni de garantir qu’aucune autre publicité n’existe. Le premier mail parle donc de publicités archivées et de leur dernière diffusion recensée. La mention « après plusieurs mois » est retirée : plusieurs historiques sont courts ou composés de périodes de diffusion discontinues.

## Niches profils et PS

Le vocabulaire est adapté aux segments ARTISAN et DIRIGEANT fournis dans les noms de fichiers, sans prétendre que chaque lecteur de l’adresse est personnellement identifié. Les prénoms des dirigeants restent des métadonnées de source ; ils ne sont pas injectés dans la salutation.

Les fichiers SOLAIRE comportent dix entreprises dont la qualification mentionne le photovoltaïque et une entreprise solaire thermique. Le PS du cas photovoltaïque est réservé à la cible solaire avec qualification photovoltaïque. Il est absent des copies PAC et rénovation. Dans SOLAIRE_DIRIGEANT, une condition Liquid liée au champ caseClientEligible évite de l’afficher pour le solaire thermique. Les deux branches ont été simulées avant import ; les valeurs relues ont été contrôlées pour tous les contacts importés.

Les PS de relance restent ceux sélectionnés : rapport disponible et possibilité de reprendre ce même fil plus tard. La signature de chaque mail est `{{sendingAccountFirstName}} de chez PolynetIA`.

## Mapping contrôlé

| Donnée source | Champ API ou variable | Usage |
| --- | --- | --- |
| email | email | Contact importé, sans duplication dans une seconde colonne email |
| entreprise | company_name → {{companyName}} | Nom de l’entreprise dans le mail |
| telephone / site | phone / website | Valeurs source conservées |
| derniere_pub | Source conservée et adStopDate | Date formatée JJ/MM/AAAA, dernière diffusion recensée |
| pubs_archivees | Source conservée et archivedAdsPhrase | Une publicité ou plusieurs, selon la ligne |
| jours_couverts / span_jours | Sources conservées ; adDuration pour les jours cumulés | Ne pas confondre diffusion cumulée et période entre première et dernière publicité |
| dirigeant_prenom / dirigeant_nom / dirigeant_qualite | Métadonnées source personnalisées | Pas de supposition sur l’identité du lecteur ; Bonjour sans prénom |
| Autres colonnes source, dont siren, niche, statut_cimetiere et fiabilite | custom_variables, noms d’origine | Traçabilité de toutes les valeurs |
| SourceLot / CampagneNiche / ICPSource | custom_variables | Fichier, cible et profil fournis |
| caseClientEligible | PV ou NO_MATCH | Condition du PS de preuve, jamais une preuve inventée |
| ResourceKey | Métier et profil de la fiche à envoyer | Choisir la bonne ressource après accord |
| Prénom de l’expéditeur | {{sendingAccountFirstName}} | Variable système, aucune colonne de lead à ajouter |

La relecture API contrôle les valeurs source, le nom d’entreprise, les champs personnalisés, la signature et la résolution locale des variables. Aucun prénom de prospect n’est nécessaire. Aucun envoi test ni prévisualisation graphique native n’a été effectué ; la délivrabilité des adresses n’a pas été vérifiée dans cette opération.

## Comptes et plafonds

Quatre comptes en état connecté, avec un prénom configuré, étaient disponibles hors campagnes actives et hors CF04/CF17. Ils sont partagés entre les huit brouillons. La somme des plafonds des nouvelles campagnes reste au maximum de 20 emails par jour pour chaque compte, sous son plafond existant de 30. Les comptes présents dans d’autres anciens brouillons devront rester pris en compte si ceux-ci sont activés plus tard.

| Segment | Compte affecté | Plafond campagne/jour |
| --- | --- | ---: |
| RENO_DIRIGEANT_part1 | [adresse privée] | 20 |
| RENO_DIRIGEANT_part2 | [adresse privée] | 20 |
| RENO_DIRIGEANT_part3 | [adresse privée] | 6 |
| RENO_ARTISAN | [adresse privée] | 6 |
| PAC_DIRIGEANT | [adresse privée] | 6 |
| PAC_ARTISAN | [adresse privée] | 6 |
| SOLAIRE_DIRIGEANT | [adresse privée] | 6 |
| SOLAIRE_ARTISAN | [adresse privée] | 6 |

Fenêtre de semaine 09h–17h, fuseau API Europe/Belgrade comme le réglage déjà utilisé pour la France métropolitaine. Arrêt sur réponse et réponse automatique ; ouvertures désactivées et liens non activés. Aucun réglage de boîte existante n’a été changé.

## Ressources d’une page préparées

Huit fiches génériques ont été préparées : PAC, rénovation, photovoltaïque et solaire thermique, en lecture terrain ou pilotage commercial. Chacune contient trois points à vérifier avec les chiffres de l’entreprise, sans présenter une fuite comme observée. Les huit PDF contiennent une page ; le rendu des deux mises en contexte représentatives a été examiné. Ces fiches restent à relire et sont à transmettre manuellement après accord.

- PAC_ARTISAN (fichier privé à transférer séparément)
- PAC_DIRIGEANT (fichier privé à transférer séparément)
- RENO_ARTISAN (fichier privé à transférer séparément)
- RENO_DIRIGEANT (fichier privé à transférer séparément)
- PV_ARTISAN (fichier privé à transférer séparément)
- PV_DIRIGEANT (fichier privé à transférer séparément)
- THERMIQUE_ARTISAN (fichier privé à transférer séparément)
- THERMIQUE_DIRIGEANT (fichier privé à transférer séparément)

## Copies utilisées selon le profil

Ces copies sont des déclinaisons de Cimetière pour revue finale. Les faits d’archive proviennent des CSV fournis. Le tableau de PS ci-dessus détermine les seuls ajouts de preuve aux variantes solaires ; aucune référence client PAC ou rénovation n’est revendiquée.

### Angle artisan

**Premier mail**

**Objet :** 📎 [META] Que deviennent vos demandes ?

> Bonjour,
>
> J’ai relevé {{archivedAdsPhrase}} pour {{companyName}} sur Meta, avec une dernière diffusion datée du {{adStopDate}}.
>
> Dans beaucoup de cas, ce n’est pas la pub qui finit par bloquer, mais ce qui se passe après le clic : délai de rappel, tri des projets, relances ou suivi des devis.
>
> Je ne vous propose pas de relancer les pubs. J’ai simplement noté 2–3 points à vérifier avant d’y remettre du budget afin de travailler la transformation des demandes en devis signés. J’ai fait cela sous la forme d’un rapport résumé en une seule page.
>
> Je vous les envoie ?
>
> {{sendingAccountFirstName}} de chez PolynetIA
>

**Relance 1**

**Objet :** même fil de discussion

> Bonjour,
>
> Je précise car mon premier mail pouvait prêter à confusion : mon sujet n’est pas les publicités Meta en soi.
>
> Quand une diffusion publicitaire s’arrête, la vraie question est souvent : est-ce que le problème venait du nombre de demandes de devis, ou de leur transformation en devis signés ?
>
> Chez {{companyName}}, c’était plutôt lequel des deux ?
>
> {{sendingAccountFirstName}} de chez PolynetIA
>
> PS : le rapport reste disponible si vous souhaitez voir les points à vérifier.
>

**Dernier suivi**

**Objet :** même fil de discussion

> Bonjour,
>
> Je clôture de mon côté après ce message.
>
> Si votre campagne publicitaire a été arrêtée volontairement et que le sujet est clos, répondez simplement « clos ».
>
> Si vous envisagez de réactiver le levier de la publicité plus tard, je peux vous envoyer un fichier recommandation en 1 page pour vérifier le parcours avant d’y remettre du budget.
>
> {{sendingAccountFirstName}} de chez PolynetIA
>
> PS : si le sujet revient plus tard, vous pouvez répondre à ce même email.
>

### Angle dirigeant

**Premier mail**

**Objet :** 🤝 [ACQUISITION] Où vont vos demandes ?

> Bonjour,
>
> J’ai relevé {{archivedAdsPhrase}} pour {{companyName}} sur Meta, avec une dernière diffusion datée du {{adStopDate}}.
>
> Dans beaucoup de cas, ce n’est pas la pub qui finit par bloquer, mais ce qui se passe après le clic : délai de rappel, qualification, relances ou suivi des devis.
>
> Je ne vous propose pas de relancer les pubs. J’ai simplement noté 2–3 points à vérifier avant d’y remettre du budget afin de optimiser le taux de conversion de vos campagnes. J’ai fait cela sous la forme d’un rapport résumé en une seule page.
>
> Je vous les envoie ?
>
> {{sendingAccountFirstName}} de chez PolynetIA
>

**Relance 1**

**Objet :** même fil de discussion

> Bonjour,
>
> Je précise car mon premier mail pouvait prêter à confusion : mon sujet n’est pas les publicités Meta en soi.
>
> Quand une diffusion publicitaire s’arrête, la vraie question est souvent : est-ce que le problème venait du volume de demandes, ou de leur transformation en chantiers signés ?
>
> Chez {{companyName}}, c’était plutôt lequel des deux ?
>
> {{sendingAccountFirstName}} de chez PolynetIA
>
> PS : le rapport reste disponible si vous souhaitez voir les points à vérifier.
>

**Dernier suivi**

**Objet :** même fil de discussion

> Bonjour,
>
> Je clôture de mon côté après ce message.
>
> Si votre campagne publicitaire a été arrêtée volontairement et que le sujet est clos, répondez simplement « clos ».
>
> Si vous envisagez de réactiver le levier de la publicité plus tard, je peux vous envoyer un fichier recommandation en 1 page pour vérifier le parcours avant d’y remettre du budget.
>
> {{sendingAccountFirstName}} de chez PolynetIA
>
> PS : si le sujet revient plus tard, vous pouvez répondre à ce même email.
>

## Identifiants locaux

Ces identifiants et les adresses d’envoi sont retirés de la copie publique. Sur un autre PC, rechercher les campagnes par les noms indiqués avant toute écriture API.

- RENO_DIRIGEANT_part1 : `[identifiant privé]`
- RENO_DIRIGEANT_part2 : `[identifiant privé]`
- RENO_DIRIGEANT_part3 : `[identifiant privé]`
- RENO_ARTISAN : `[identifiant privé]`
- PAC_DIRIGEANT : `[identifiant privé]`
- PAC_ARTISAN : `[identifiant privé]`
- SOLAIRE_DIRIGEANT : `[identifiant privé]`
- SOLAIRE_ARTISAN : `[identifiant privé]`

**Validation finale et lancement :** les huit campagnes sont en brouillon. Le fondateur relira les objets, les déclinaisons et les ressources avant tout lancement manuel. La relance d’observation reste hors séquence.
