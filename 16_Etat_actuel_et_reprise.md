# État actuel de la stratégie et reprise du travail

Mis à jour le 20 novembre 2026. Lire ce document au début d’une reprise. Il présente les dernières décisions ; les anciennes mentions « en attente » dans les documents historiques ne remplacent pas les validations résumées ici.

## 1. Agence offre et preuve

PolynetIA propose un système d’acquisition client aux entreprises du photovoltaïque, de la PAC et de la rénovation, en France. Les cibles sont des artisans et des dirigeants ; les deux profils peuvent se recouper. Aucun prix au premier contact. La rémunération envisagée combine mise en place, mensuel et pourcentage de croissance attribuable, avec les modalités à déterminer après qualification.

Le fondateur a confirmé avoir accompagné **une entreprise photovoltaïque**, avec campagnes publicitaires ciblées et qualification des demandes. Le cas reste anonyme. Les résultats chiffrés, le budget, la période et le détail des canaux effectivement utilisés restent à documenter. Ne pas inventer de référence client PAC ou rénovation, de chantiers signés ou de garantie.

## 2. Campagnes et validations

| Campagne | Validations explicites | Éléments encore proposés |
| --- | --- | --- |
| CF04 cas client | Template principal du mail 1, template de relance 2, signature de chez PolynetIA, preuve photovoltaïque et projection vers le métier ciblé ; objet photovoltaïque choisi et appliqué | Déclinaisons concrètes, relances 1 et 3 et réponse manuelle après accord |
| CF17 étude sectorielle | Choix du template, ajout de trois bénéfices maximum, sujet de l’étude : points de fuite dans l’acquisition de la niche ciblée ; objet étude choisi et appliqué | Formulations finales de la séquence et réponse manuelle après accord |
| Cimetière publicités Meta arrêtées | Séquence de prospection revue dans le chat, relances 1 à 3, ouverture affirmative de la relance 2 et quatre PS sélectionnés | Déclinaisons finales et données vérifiées pour chaque prospect, réponse manuelle après accord |
| Salaire fantôme recrutement ancien | Méthode retenue et consigne de fusionner le premier mail avec l’ancienne première relance | Texte fusionné et suite de la séquence à valider |

Les quatre PS Cimetière sélectionnés et leurs conditions sont repris dans [le guide de rédaction](15_Guide_redaction_objets_mails_PS.md). Les anciens blocs proposant trois PS par message dans la fiche 09 sont des historiques de choix, pas une nouvelle demande de validation des quatre sélections déjà faites.

Les règles et lexiques des fiches 11 à 13 sont créés ; la consultation systématique est demandée. Les choix détaillés de vocabulaire et nouvelles formulations artisans/dirigeants restent à valider. Ne pas déduire le profil des seules classes d’effectif.

## 3. Brouillons réellement préparés dans Instantly

Deux campagnes ont été créées par API, sans activation :

| Nom à rechercher dans Instantly | Source | Contacts importés | Contacts déjà présents écartés |
| --- | --- | ---: | ---: |
| [A VALIDER] CF04 \| Cas client \| PV \| ICP mixte \| lot 001 | PV_0-5, lot 001 | 38 | 12 |
| [A VALIDER] CF17 \| Etude sectorielle \| PV \| ICP mixte \| lot 002 | PV_0-5, lot 002 | 39 | 11 |

Les deux lots contenaient initialement 50 contacts chacun. Les sources locales sont conservées. Aucun doublon entre les deux nouveaux groupes n’a été détecté. Le rôle des contacts reste non confirmé ; aucun email ne les présente automatiquement comme artisans ou dirigeants.

Les huit textes et paramètres enregistrés figurent dans [la fiche des brouillons](14_Brouillons_Instantly_CF04_CF17.md). Les délais vers les étapes suivantes sont 3, 3 et 4 jours. Les campagnes utilisent chacune une boîte distincte, sans affectation à une campagne active lors du contrôle. Le plafond de chaque campagne est 20 emails par jour, avec 10 nouveaux contacts maximum ; arrêt sur réponse, suivi des ouvertures et liens désactivé. La délivrabilité des adresses n’a pas été vérifiée dans cette opération.

La relecture API a confirmé le texte enregistré, les variables utilisées, les champs importés et le statut brouillon. Le fondateur effectuera lui-même le lancement manuel après validation. Les copies inscrites dans un brouillon ne sont pas pour autant toutes approuvées.

## 4. Objets validés et enregistrés

Le format demandé est : emoji 🤝 ou 📎, un mot-clé entre crochets, une question courte de trois à cinq mots. Les douze propositions sont conservées dans la fiche 15. Le fondateur a validé les deux choix suivants, appliqués et relus par API le 20 novembre :

- **CF04 : 🤝 [PHOTOVOLTAÏQUE] Vos demandes mieux qualifiées ?**
- **CF17 : 📎 [ÉTUDE] Des fuites à vérifier ?**

Seuls les objets du premier mail ont été remplacés. Les relances conservent leur objet vide de configuration pour rester dans le même fil. Les corps, délais, comptes et paramètres de suivi sont inchangés. Les deux campagnes restent en brouillon ; la validation des objets ne vaut pas validation de toutes les copies ni autorisation de lancement.

Le token du nom d’entreprise est `{{companyName}}`, pas `{{company_name}}`. L’objectif de taux d’ouverture ne doit pas être présenté comme un résultat acquis. Ne pas activer automatiquement le suivi des ouvertures pour mesurer les nouvelles propositions.

## 5. Données de segmentation

Le travail local compte 10 950 contacts dans 225 fichiers : 216 lots complets et 9 reliquats. Les métiers sont PAC, photovoltaïque, chauffage au bois, ventilation, solaire thermique et un groupe AUTRE à qualifier. Les classes de taille 0–5 et 6–19 existent pour PAC, PV et bois. Aucun segment autonome rénovation générale ou climatisation n’est identifié.

La répartition agrégée est dans [Segmentation_Instantly.md](Segmentation_Instantly.md). Les CSV, coordonnées individuelles et exports API sont des données privées ; ils ne font pas partie de la publication GitHub publique.

## 6. Ordre de reprise

**Signature validée et appliquée :** `{{sendingAccountFirstName}} de chez PolynetIA`. Le fondateur a choisi le prénom seul configuré sur chaque boîte, pour les huit mails CF04/CF17 et toutes les futures campagnes. Les huit signatures sont modifiées et relues par API ; les prénoms des deux comptes sont présents et les simulations locales les résolvent. Les objets et autres contenus sont conservés, les campagnes restent en brouillon. Aucun envoi test n’a été effectué.

**Nouvelle demande en cours :** choisir deux autres méthodes de campagne. Cinq approches issues des modèles du mentor sont proposées : audit vidéo personnalisé (CF24/ED04), interview de recherche (CF21), podcast (PO01/PO02), atelier pédagogique (CF14), offre directe avec appel court (CF03). Aucune de ces nouvelles approches n’est encore choisie ni configurée dans cette étape.

**Priorité suivante demandée :** préparer trois variantes inspirées du Mom Test, puis suivre la structure précisée par le fondateur : compréhension du métier, promesse de valeur, question sur les difficultés et PS de compréhension. La version 2 proposée dans [la fiche 17](17_Campagne_Mom_Test_variantes.md) porte sur la dernière action pour trouver des clients, la dernière demande reçue et le dernier devis envoyé. Les questions recherchent des faits récents ; la présentation de la promesse rend cette structure distincte d’un entretien Mom Test strict. Le PS proposé est limité au premier mail et ne déclare pas la démarche globale sans intérêt commercial. La cible est le photovoltaïque ; les formulations attendent validation. Aucun setup ni changement des campagnes existantes n’est effectué pour cette nouvelle méthode.

1. Lire AGENTS.md, ce document, la fiche 15 et les règles 11.
2. Prendre connaissance des copies réellement enregistrées dans la fiche 14 et de leur état de validation.
3. Conserver les objets CF04 et CF17 déjà validés et terminer la revue des textes et des lexiques.
4. Décliner ensuite les templates par métier et profil étayé, en conservant le cas photovoltaïque et une projection distincte pour les autres niches.
5. Avant une modification Instantly, lire les campagnes via l’API et retrouver celles portant les noms ci-dessus. Ne pas recréer les brouillons parce que les identifiants locaux manquent sur un nouveau PC.
6. Prévisualiser les variables et vérifier les ressources promises, puis laisser le fondateur lancer manuellement.

Les nouvelles listes Cimetière et Salaire fantôme étaient préparées avec Claude ; elles n’ont pas été reçues ici. Les observations de publicités, recrutements et parcours doivent être vérifiées avant leur utilisation.

## 7. Ce que le dépôt public permet de reprendre

Le dépôt rassemble la stratégie, les modèles textuels, les règles, les guides, les états de validation et les copies préparées. Les ressources binaires originales, les CSV de leads et les exports privés du compte restent à transférer séparément si nécessaires. La clé Instantly doit être fournie localement par variable d’environnement sur le nouvel ordinateur ; elle n’est jamais publiée.
