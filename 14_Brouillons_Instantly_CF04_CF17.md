# Brouillons Instantly CF04 et CF17

État vérifié par API le 20 novembre 2026 : les deux campagnes sont en brouillon (status 0). Aucun appel d’activation ni envoi test n’a été effectué. Les autres campagnes ont conservé leur statut lors du contrôle.

## Cible et profil

Les deux campagnes utilisent des lots distincts du segment PV_0-5 : installateurs photovoltaïques. Les fonctions ne sont pas assimilées à la taille. L’angle reste commun aux artisans et dirigeants dont les responsabilités ne sont pas confirmées ; ICPStatus est renseigné non_confirme. Les nouvelles déclinaisons restent soumises à la validation manuelle du fondateur. Les deux objets affichés ci-dessous ont été explicitement validés, appliqués et relus par API.

CF17 reprend le sujet précisé par le fondateur : les principaux points de fuite dans l’acquisition client des entreprises de la niche ciblée. Aucun constat chiffré ni résultat de l’étude n’a été ajouté.

## Paramètres enregistrés

- Quatre mails par campagne ; délais vers le mail suivant : 3, 3 et 4 jours, unité days. Le délai appartient à l’étape précédente dans l’API.
- Lundi à vendredi, 09h–17h. Fuseau API Europe/Belgrade, repris du réglage existant et correspondant à l’heure de France métropolitaine. Europe/Paris ne figure pas dans les valeurs admises du schéma API actuel.
- Plafond par campagne : 20 emails par jour, dont au maximum 10 nouveaux contacts. Plafond existant des boîtes : 30, inchangé. Une boîte distincte par campagne, sans affectation à une campagne active au contrôle.
- Arrêt sur réponse et réponse automatique ; suivi des ouvertures et liens désactivé ; mode texte ; en-tête de désinscription activé.
- Import avec skip_if_in_workspace=true et respect de la liste de blocage du compte. Vérification de délivrabilité des adresses non déclenchée.

## Mapping contrôlé

| Colonne CSV | Champ API | Usage |
| --- | --- | --- |
| Email | email | Adresse du contact |
| CompanyName | company_name, relu dans payload.companyName | Variable de lead utilisée dans les mails : {{companyName}} |
| Prénom du compte expéditeur | Variable système {{sendingAccountFirstName}} | Signature validée : {{sendingAccountFirstName}} de chez PolynetIA ; aucune colonne de lead ajoutée |
| FirstName / LastName | first_name / last_name | Valeurs conservées ; salutation Bonjour sans prénom |
| JobTitle | job_title | Fonction du contact ; aucune attribution automatique artisan/dirigeant |
| Phone / Website | phone / website | Données conservées |
| Location, Linkedin, Greeting, Segment, Activity, ServiceHook, TeamSize, Department, SIRET, MailboxType | custom_variables avec les mêmes noms | Métadonnées relues, non affichées automatiquement dans le copy |
| SourceLot / CibleMetier / ICPStatus | custom_variables | Lot d’origine / Photovoltaïque / non_confirme |

Tous les champs des leads importés ont été relus et comparés aux sources. Aucun repère éditorial entre crochets ni variable non résolue ne subsiste dans les simulations locales à partir des données relues. Les CSV sources sont inchangés. Les prénoms configurés ont été vérifiés pour chaque compte affecté. La variable système est documentée par Instantly ; aucun envoi test ni prévisualisation graphique native n’a été exécuté dans cette opération.

JobTitle est importé via le champ natif job_title pour éviter une collision avec un champ personnalisé équivalent. Une ancienne définition personnalisée JobTitle, inutilisée par le copy, peut rester visible dans CF04 après le premier essai de mapping ; aucune seconde valeur de fonction n’a été importée.

## Ressources et validation avant lancement manuel

Le cas photovoltaïque en une page, l’étude sectorielle et la vidéo sont proposés sur accord. Ils ne sont pas joints ni envoyés automatiquement. Leurs envois et les réponses positives restent manuels. Le fondateur doit relire les copies ci-dessous et les ressources promises avant son lancement manuel. La création technique en brouillon ne vaut pas validation de toutes les nouvelles formulations.

## CF04

**Nom dans Instantly :** [A VALIDER] CF04 | Cas client | PV | ICP mixte | lot 001

**Identifiant :** [identifiant privé]

**Statut :** brouillon, 0. **Contacts présents :** 38 sur 50 proposés. **Déjà présents et écartés :** 12. **Compte :** [adresse privée].

**Fichier source :** Leads_Instantly\01_Lots_50\PV_0-5\PV_0-5__lot_001__50_leads.csv

### Mail 1 — J0

**Objet :** 🤝 [PHOTOVOLTAÏQUE] Vos demandes mieux qualifiées ?

> Bonjour,
>
> Nous aidons les installateurs photovoltaïques à structurer leur acquisition et la qualification de leurs demandes.
>
> Nous avons récemment accompagné une entreprise d’installation photovoltaïque en mettant en place des campagnes publicitaires ciblées et un système de qualification des leads.
>
> Je peux vous envoyer le document en une seule page présentant ce cas client et le système installé.
>
> Il suffit de répondre « oui » et je vous l’envoie.
>
> {{sendingAccountFirstName}} de chez PolynetIA
>

### Relance 1 — J+3

**Objet :** même fil de discussion

> Bonjour,
>
> Je voulais simplement m’assurer que mon dernier email ne s’était pas perdu dans votre boîte de réception.
>
> {{sendingAccountFirstName}} de chez PolynetIA
>

### Relance 2 — J+6

**Objet :** même fil de discussion

> Bonjour,
>
> Nous avons récemment accompagné une entreprise d’installation photovoltaïque en mettant en place des campagnes publicitaires ciblées et un système de qualification des demandes.
>
> Cette même approche peut s’adapter à votre activité d’installation photovoltaïque : attirer des demandes dans votre zone d’intervention et qualifier les projets selon le type de bâtiment, la localisation et le projet envisagé.
>
> Le document présente en une seule page le cas client et le système installé.
>
> Souhaitez-vous que je vous l’envoie ?
>
> {{sendingAccountFirstName}} de chez PolynetIA
>

### Relance 3 — J+10

**Objet :** même fil de discussion

> Bonjour,
>
> Je voulais vérifier une dernière fois, au cas où mes emails se seraient perdus dans votre boîte de réception.
>
> Si ce n’est pas le bon moment pour {{companyName}} de travailler sur les demandes de devis et leur suivi, dites-le-moi simplement.
>
> Bonne continuation,
>
> {{sendingAccountFirstName}} de chez PolynetIA
>

**Vérifications API :** statut brouillon, texte et paramètres conformes, mapping sans erreur, nombre de contacts rapproché de l’import, sources inchangées.

## CF17

**Nom dans Instantly :** [A VALIDER] CF17 | Etude sectorielle | PV | ICP mixte | lot 002

**Identifiant :** [identifiant privé]

**Statut :** brouillon, 0. **Contacts présents :** 39 sur 50 proposés. **Déjà présents et écartés :** 11. **Compte :** [adresse privée].

**Fichier source :** Leads_Instantly\01_Lots_50\PV_0-5\PV_0-5__lot_002__50_leads.csv

### Mail 1 — J0

**Objet :** 📎 [ÉTUDE] Des fuites à vérifier ?

> Bonjour,
>
> J’ai récemment terminé une étude sur les principaux points de fuite dans l’acquisition client des installateurs photovoltaïques.
>
> Notre système vise trois bénéfices :
>
> – Attirer des demandes correspondant à votre zone et à vos prestations.
>
> – Qualifier les projets selon vos critères.
>
> – Organiser les relances et le suivi des devis.
>
> Je ne sais pas si cela peut vous intéresser, mais je voulais tenter ma chance. Faites-moi savoir et je vous l’enverrai.
>
> {{sendingAccountFirstName}} de chez PolynetIA
>

### Relance 1 — J+3

**Objet :** même fil de discussion

> Bonjour,
>
> Je voulais simplement m’assurer que mon dernier email ne s’était pas perdu dans votre boîte de réception.
>
> {{sendingAccountFirstName}} de chez PolynetIA
>

### Relance 2 — J+6

**Objet :** même fil de discussion

> Bonjour,
>
> J’ai également une courte vidéo présentant les mécanismes de notre système d’acquisition et de qualification des demandes.
>
> Souhaitez-vous la recevoir pour comprendre plus concrètement notre approche ?
>
> Vous pourrez ensuite décider si cela vaut la peine d’en discuter.
>
> {{sendingAccountFirstName}} de chez PolynetIA
>

### Relance 3 — J+10

**Objet :** même fil de discussion

> Bonjour,
>
> Je voulais vérifier une dernière fois, au cas où mes emails se seraient perdus dans votre boîte de réception.
>
> Si le sujet des demandes de devis et de leur suivi n’est pas une priorité actuelle chez {{companyName}}, dites-le-moi simplement.
>
> Bonne continuation,
>
> {{sendingAccountFirstName}} de chez PolynetIA
>

**Vérifications API :** statut brouillon, texte et paramètres conformes, mapping sans erreur, nombre de contacts rapproché de l’import, sources inchangées.

## Références techniques

[Création de campagne](https://developer.instantly.ai/api-reference/campaign/create-campaign), [import des leads](https://developer.instantly.ai/api-reference/lead/add-leads-in-bulk-to-a-campaign-or-list).
