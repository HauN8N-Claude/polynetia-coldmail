# Mapping et organisation des envois Instantly

**Préparation API du 20 novembre 2026 :** consulter [les deux brouillons CF04 et CF17](14_Brouillons_Instantly_CF04_CF17.md) pour les réglages effectivement enregistrés, les 77 contacts importés et le mapping contrôlé par relecture. Dans cette opération API, `JobTitle` est transmis au champ natif `job_title`, sans seconde valeur personnalisée équivalente. `CompanyName` devient `company_name` et alimente `{{companyName}}`. Les tableaux d’import UI historiques ci-dessous restent des références pour leurs propres modes d’import. Les nouvelles campagnes sont en brouillon ; leur activation appartient au fondateur.

Règles de préparation du 19 novembre 2026. Elles s’appliquent aux campagnes CF04, CF17, Cimetière et Salaire fantôme, issues des sources retenues. La fiche 09 a été révisée avec les nouvelles copies à valider ; les premiers essais libres restent historiques. Aucun réglage réel d’Instantly n’a été modifié dans ce travail.

## 1. Contraintes confirmées par le fondateur

- Les variables doivent correspondre au mapping réellement importé dans Instantly.
- Chaque relance de prospection doit attendre au moins trois jours après le précédent message sortant du même suivi.
- Les campagnes simultanées doivent disposer d’une répartition des boîtes et d’un budget d’envoi cohérents, incluant les relances.

Ces règles restent applicables aux prochaines modifications du copy. Une nouvelle recommandation du fondateur sera enregistrée dans le registre puis intégrée ici ou dans sa section de référence.

## 2. Schéma des fichiers vérifié

Les 225 lots CSV ont été lus : 10 950 contacts, 17 colonnes identiques dans le même ordre, aucun en-tête divergent. Les champs Email et CompanyName ne sont pas vides. FirstName et LastName sont vides pour 9 299 contacts ; les identités présentes ne sont pas toutes confirmées. Le contrôle porte sur les données du fichier, pas sur l’existence des adresses ou la configuration d’un import déjà effectué.

Le premier contrôle concernait les anciennes copies sans variable de lead. Les nouvelles séquences de la fiche 09 utilisent companyName et des champs de signal personnalisés. Elles commencent par « Bonjour, » et contiennent encore des repères éditoriaux de signature et de réponse manuelle. Les listes Cimetière et Salaire fantôme ne sont pas reçues ; leur mapping n’est donc pas encore vérifié sur des fichiers réels.

## 3. Table de mapping

À l’import, sélectionner les champs prédéfinis dans le menu Instantly. Le nom de la colonne source ne devient pas automatiquement le nom d’un champ prédéfini. Pour les champs personnalisés, conserver exactement l’orthographe et la casse du CSV. Insérer les variables depuis le sélecteur de l’éditeur, puis contrôler le rendu.

| Colonne CSV | Champ à sélectionner dans Instantly | Usage dans le copy |
| --- | --- | --- |
| Email | Email, prédéfini et obligatoire | Destinataire ; pas nécessaire dans le corps |
| FirstName | First name, prédéfini | `{{firstName}}` uniquement après confirmation de l’identité ; sinon « Bonjour, » |
| LastName | Last name, prédéfini | Facultatif ; variable à insérer via le sélecteur si nécessaire |
| CompanyName | Company name, prédéfini | `{{companyName}}` si la phrase a été validée avec les valeurs réelles |
| JobTitle | Job title, prédéfini | Facultatif ; insérer via le sélecteur si utilisé |
| Phone | Phone, prédéfini | Donnée de contact, pas utilisée par les copies actuelles |
| Website | Website, prédéfini | Facultatif ; ne pas en déduire une analyse déjà effectuée |
| Location | Location, prédéfini | Facultatif ; ne pas transformer automatiquement ce champ en ville seule |
| Linkedin | LinkedIn, prédéfini | Donnée source, pas utilisée par les copies actuelles |
| Greeting | Custom variable nommée Greeting | `{{Greeting}}`, conservée mais non utilisée tant que l’identité n’est pas validée |
| Segment | Custom variable nommée Segment | `{{Segment}}`, utile au suivi plutôt qu’au texte public |
| Activity | Custom variable nommée Activity | `{{Activity}}` seulement après contrôle des libellés |
| ServiceHook | Custom variable nommée ServiceHook | `{{ServiceHook}}` seulement après contrôle de la grammaire de la phrase complète |
| TeamSize | Custom variable nommée TeamSize | `{{TeamSize}}`, donnée de segmentation ; ne démontre pas un besoin |
| Department | Custom variable nommée Department | `{{Department}}` si utilisé ; conserver les zéros initiaux |
| SIRET | Custom variable nommée SIRET | `{{SIRET}}`, identifiant de rapprochement, pas de personnalisation prévue |
| MailboxType | Custom variable nommée MailboxType | `{{MailboxType}}`, information interne plutôt que texte public |

Les champs non utilisés peuvent rester non importés si la campagne n’en a pas besoin, en conservant le CSV source complet. Ne pas créer une deuxième variable personnalisée qui concurrence un champ prédéfini. Les tokens des modèles bruts du mentor, comme les champs de niche ou de ville absents du CSV, ne sont pas directement utilisables sans adaptation.

La signature correspond à l’expéditeur réel de la boîte choisie, pas au prénom du prospect. La contrôler en sélectionnant chaque compte d’envoi dans la prévisualisation. Une variable n’est ajoutée au copy qu’après vérification du champ importé, des valeurs et du rendu sur plusieurs contacts. Si une donnée manque, employer une phrase complète sans cette personnalisation plutôt que laisser une salutation ou une proposition tronquée.

**Choix du fondateur appliqué le 20 novembre :** signer `{{sendingAccountFirstName}} de chez PolynetIA` dans les huit mails CF04/CF17 et les futures campagnes. Ce token est une variable système du compte expéditeur, sans colonne CSV ni variable personnalisée de lead à créer. Vérifier le prénom configuré pour toutes les boîtes affectées ; ne pas remplacer le token par le prénom du prospect. La relecture API confirme les huit signatures ; les simulations de résolution utilisent les prénoms réellement configurés. Aucun envoi test n’est déclenché. Référence : [variables système Instantly](https://help.instantly.ai/en/articles/6687668-liquid-syntax).

Référence : [variables et prévisualisation Instantly](https://help.instantly.ai/en/articles/6135930-how-to-add-and-use-variables-in-campaigns).

### Champs supplémentaires pour les nouvelles listes

Les noms proposés pour les champs personnalisés sont `adStopDate`, `adDuration`, `observedFunnelSignal`, `openRoleTitle`, `daysOnline` et `jobGoal`, avec cette casse exacte. Leurs définitions et critères d’emploi figurent en section 7 de la fiche 09. Les en-têtes fournis par Claude seront rapprochés de ces noms avant import, sans écraser les champs sources.

Choix final du 20 novembre : la relance 2 de Cimetière utilise l’ouverture affirmative et le champ personnalisé `observedFunnelSignal`, avec cette casse exacte. Il est obligatoire pour cette relance et doit contenir une observation réelle, vérifiée et pertinente du parcours. Si le champ est vide ou non vérifié, ne pas envoyer le message ; ne pas utiliser une valeur de remplacement générique. Aucun champ de comptage de campagnes ou d’annonces n’est introduit sans donnée correspondante.

`openRoleTitle` désigne le poste à pourvoir ; le `JobTitle` du CSV historique désigne la fonction du contact. Ils doivent rester distincts. Conserver les URL et dates de vérification des annonces et publicités dans les données de travail. Les champs inconnus ne reçoivent aucune date, durée, cause ou observation inventée.

Les créneaux et les interprétations dans les réponses manuelles sont renseignés après lecture de la conversation ; ils ne sont pas traités comme des variables automatiques déjà remplies pour tout le fichier.

## 4. Attente entre les relances

Le minimum du fondateur est **trois jours calendaires complets**, soit au moins 72 heures depuis le précédent message concerné. Les réponses à une nouvelle question du prospect et les confirmations de rendez-vous demandé sont des échanges distincts des relances de prospection ; elles peuvent être traitées rapidement.

Pour une séquence de trois messages si elle est retenue, le repère de préparation reste :

| Transition | Attente à configurer | Repère sans report de calendrier |
| --- | ---: | --- |
| Premier email vers relance 1 | 4 jours après l’envoi effectif du premier email | J+4 |
| Relance 1 vers relance 2 | 6 jours après l’envoi effectif de la relance 1 | J+10 si la relance 1 n’a pas été reportée |

Ne pas saisir dix jours comme délai entre la relance 1 et la relance 2 si le souhait est une dernière relance autour de J+10. Instantly applique l’attente par contact à partir de l’étape précédente, en jours calendaires, puis selon le créneau d’envoi. Un report peut donc décaler les dates finales sans raccourcir l’intervalle.

Pour Cimetière et Salaire fantôme, le nouveau Word prévoit quatre messages : attendre trois jours après le premier, trois jours après la relance 1, puis quatre jours après la relance 2. Les repères sans report sont J0, J+3, J+6 et J+10. Les délais sont toujours calculés depuis les envois effectifs, et respectent le minimum du fondateur.

Pour le suivi après remise d’un document : première relance au moins trois jours après l’envoi effectif du document ; suivante au moins trois jours après la première relance. Même minimum pour une nouvelle relance de reprogrammation après un rendez-vous manqué. Un report explicite du prospect prime s’il demande une date plus lointaine.

Contrôler chaque transition dans chaque variante. Une réponse humaine interrompt la séquence froide. Les délais à 48 heures ou deux jours présents dans les documents du mentor restent des textes sources et ne sont pas repris dans les cadences PolynetIA.

Référence : [calcul des délais entre étapes Instantly](https://help.instantly.ai/en/articles/7916860-time-to-wait-between-steps).

## 5. Répartition des boîtes entre campagnes

La répartition réelle sera construite à partir des comptes disponibles. Aucun inventaire actuel des boîtes, fournisseurs, plafonds, rampes ou campagnes actives n’est confirmé dans le dossier. Les quinze boîtes citées par le mentor ne sont pas considérées comme appartenant à PolynetIA.

### Organisation privilégiée

Quand les comptes disponibles le permettent, attribuer des groupes dédiés aux quatre familles CF04, CF17, Cimetière et Salaire fantôme, sans sélectionner toutes les boîtes dans toutes les campagnes. Si un test exploratoire est réactivé avec des templates conformes, lui réserver également une capacité identifiée.

Si le nombre de boîtes impose un partage, fixer le budget de chaque campagne avant lancement. Le plafond d’une boîte reste global à ses campagnes. Les campagnes programmées plus tôt peuvent consommer sa capacité avant les autres ; contrôler ensemble les horaires et l’utilisation quotidienne. Références : [limites de comptes et campagnes](https://help.instantly.ai/en/articles/6248612-account-and-campaign-limits), [diagnostic des campagnes qui n’envoient pas](https://help.instantly.ai/en/articles/5975337-campaign-not-sending-complete-troubleshooting-guide).

### Budget à construire

Pour chaque boîte, relever le domaine, le fournisseur, la disponibilité, le plafond configuré, le plafond effectif de montée en charge, les autres usages et les campagnes déjà associées. Pour un domaine regroupant plusieurs boîtes, examiner aussi la charge cumulée et les incidents ; trois boîtes ne sont pas trois réputations indépendantes.

Pour chaque jour, la somme des premiers emails et des relances prévus sur une boîte doit tenir dans sa capacité disponible. Les premiers contacts sont réduits lorsque les relances dues augmentent. Un lot de cinquante personnes ne se traduit pas par seulement cinquante envois si deux relances sont prévues.

| Campagne | Groupe de comptes | Budget premiers emails et relances | État |
| --- | --- | --- | --- |
| CF04 — Cas client | À attribuer depuis l’inventaire réel | À calculer | Template retenu |
| CF17 — Étude sectorielle | À attribuer depuis l’inventaire réel | À calculer | Template retenu |
| Cimetière | À attribuer depuis l’inventaire réel | À calculer | Copy à valider et leads attendus |
| Salaire fantôme | À attribuer depuis l’inventaire réel | À calculer | Copy à valider et leads attendus |

Contrôler aussi l’espacement global entre deux envois d’une même boîte, sa connexion, le créneau et le fuseau. Garder une marge de fonctionnement choisie après inventaire ; ne pas remplir mécaniquement toute la capacité théorique. Les réponses manuelles et rappels ne relèvent pas forcément du même compteur produit, mais ils font partie de l’activité réelle de la messagerie.

Les allocations de contacts restent distinctes de celles des expéditeurs : une bonne répartition des boîtes ne corrige pas un contact présent dans plusieurs campagnes.

## 6. Contrôle avant activation

Vérifier sur les versions finales :

1. Mapping de l’email et des champs effectivement utilisés, avec casse exacte des variables personnalisées.
2. Rendu sur plusieurs contacts, dont champs vides et boîtes génériques, puis sur chaque compte d’envoi.
3. Remplacement des repères de signature et de lien ; aucune accolade ou balise non résolue dans l’email final.
4. Attente minimale de trois jours à chaque transition de relance et prise en compte du calendrier réel.
5. Comptes affectés, capacités partagées, charge des relances et budgets des campagnes simultanées.
6. Arrêt sur réponse, exclusions communes et absence de chevauchement des contacts.
7. Test d’envoi et de réponse avec des adresses contrôlées, puis examen des activités prévues par l’outil.

Les contrôles locaux du CSV et la documentation du produit ne remplacent pas ces essais dans le compte réel. La stratégie de copy peut continuer pendant la préparation de cet inventaire et de ces réglages.
