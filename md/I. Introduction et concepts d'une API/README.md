# I. Introduction et concepts d'une API

## 1. Définition d'une API

* Qu’est-ce qu’une Application Programming Interface ?
* À quoi sert une API dans le développement logiciel ?
* Métaphore : API comme un menu de restaurant

## 2. Types d’API

* REST (REpresentational State Transfer)
  * Architecture orientée ressource
  * Stateless, utilisation d’URL + méthodes HTTP
* GraphQL (bref aperçu)
* SOAP (bref aperçu)
* Pourquoi on choisit REST dans ce cours

## 3. Formats de données

* JSON : format léger, structuré en paires clé-valeur
* XML : format plus verbeux (non utilisé ici)
* Pourquoi JSON est majoritaire dans les APIs web

## 4. Méthodes HTTP

* GET : lire une ressource
* POST : créer une ressource
* PUT : mettre à jour (écraser)
* PATCH : mettre à jour partiellement
* DELETE : supprimer

## 5. Codes de retour HTTP

* 200 OK
* 201 Created
* 204 No Content
* 400 Bad Request
* 401 Unauthorized / 403 Forbidden
* 404 Not Found
* 500 Internal Server Error
