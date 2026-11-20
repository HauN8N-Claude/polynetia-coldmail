# Consignes du dossier PolynetIA

## Sécurité des suppressions

- Ne jamais employer `rm -rf`.
- Employer `trash` pour une suppression afin de conserver une possibilité de récupération.

## Rédaction de coldmail et de templates

- Au début d’une reprise, lire `16_Etat_actuel_et_reprise.md` pour les dernières validations, qui priment sur les mentions historiques.
- Avant toute création ou modification d’objet, mail, relance, PS, réponse ou template coldmail, lire `11_Regles_redaction_coldmail.md`.
- Consulter `15_Guide_redaction_objets_mails_PS.md` pour les formats, exemples et statuts des objets, corps de mails et PS.
- Lire ensuite `12_ICP_Artisans.md` ou `13_ICP_Dirigeants.md` selon le profil étayé ; lire les deux si le profil est mixte ou inconnu.
- Consulter le template source dans `07_Templates_emails_du_mentor.md` et la dernière version validée dans `09_Trois_campagnes_PolynetIA.md` ; les instructions directes les plus récentes du fondateur priment.
- Traiter les lexiques et exemples des fiches 12 et 13 comme des propositions tant que le fondateur ne les a pas validés. Leur consultation est obligatoire ; elle ne vaut pas approbation de leurs formulations.
- Distinguer activité, responsabilité et taille. Ne pas déduire artisan/dirigeant des seuils 0–5 ou 6–19 salariés ni d’une adresse email générique.
- Conserver le cas client photovoltaïque ; adapter séparément la projection dans le métier du prospect. Aucun résultat en PAC, bois, ventilation, thermique ou rénovation n’est confirmé à ce stade.
- Garder les critères et noms de métier comme textes éditoriaux avant leur validation ; toute variable d’import suit la fiche `10_Parametrage_Instantly.md`.
- Présenter les déclinaisons nouvelles pour validation, sans écraser spontanément un texte déjà approuvé ni lancer d’envoi.

## Configuration Instantly

- Utiliser l’API Instantly avec la variable d’environnement `INSTANTLY_API_KEY` déjà configurée ; ne jamais afficher sa valeur ni l’écrire dans un fichier.
- Pour CF04 et CF17, conserver les campagnes en brouillon. Le fondateur effectuera lui-même le lancement manuel après validation ; ne pas appeler un endpoint d’activation ou d’envoi test.
- Avant une reprise après erreur API, relire l’état distant ; réutiliser les identifiants enregistrés et les clés d’idempotence d’import plutôt que recréer ou réimporter à l’aveugle.
- Consulter `14_Brouillons_Instantly_CF04_CF17.md` pour les noms des campagnes, copies enregistrées, lots, mapping et comptes de cette préparation.

## Publication GitHub

- Publier la stratégie et les documents de travail demandés, sans clé, fichier de leads, coordonnées de contacts, export API ou configuration privée.
- Dans une copie publique, rechercher les brouillons Instantly par leurs noms et par lecture API ; ne pas publier les identifiants internes ni recréer les campagnes lors d’une reprise.
