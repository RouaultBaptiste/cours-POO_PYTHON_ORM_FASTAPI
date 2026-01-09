![logo-diginamic](../img/logo-diginamic.png)

<br>

# 📘 **Codes de retour HTTP**

<br>

## **<u>Sommaire</u>**

- [📘 **Codes de retour HTTP**](#-codes-de-retour-http)
  - [**Sommaire**](#sommaire)
  - [**🧭 Comment une API communique ?**](#-comment-une-api-communique-)
  - [**🧮 Les grandes familles de codes HTTP**](#-les-grandes-familles-de-codes-http)
  - [**🧠 Codes courants à connaître en API**](#-codes-courants-à-connaître-en-api)
  - [🐱 http.cat](#-httpcat)
  - [**📌 À retenir**](#-à-retenir)

<div style="page-break-after: always;"></div>

## **🧭 <u>Comment une API communique ?</u>**

Quand on utilise une API, chaque requête reçoit une **réponse contenant deux choses** :

* **Des données** (optionnelles)
* Un **code de retour HTTP** qui décrit le résultat de l’opération

<br>

## **🧮 <u>Les grandes familles de codes HTTP</u>**

| Famille | Signification                | Exemple               |
| ------: | ---------------------------- | --------------------- |
|   `1xx` | ℹ️ Information (peu utilisé) | 100 Continue          |
|   `2xx` | ✅ Succès                     | 200 OK, 201 Created   |
|   `3xx` | 🔁 Redirection               | 301 Moved Permanently |
|   `4xx` | ⚠️ Erreur côté client        | 400, 401, 403, 404    |
|   `5xx` | ❌ Erreur côté serveur        | 500, 503              |

<br>

## **🧠 <u>Codes courants à connaître en API</u>**

| Code | Nom                   | Signification                                               |
| ---- | --------------------- | ----------------------------------------------------------- |
| 200  | OK                    | La requête a réussi et renvoie des données                  |
| 201  | Created               | Une ressource a été créée (ex : `POST /users`)              |
| 204  | No Content            | Opération réussie mais pas de données à renvoyer (`DELETE`) |
| 400  | Bad Request           | Requête invalide (données manquantes, erreur de format)     |
| 401  | Unauthorized          | L’utilisateur n’est pas authentifié                         |
| 403  | Forbidden             | Authentifié mais pas autorisé à faire cette action          |
| 404  | Not Found             | Ressource introuvable                                       |
| 500  | Internal Server Error | Erreur technique sur le serveur                             |

<div style="page-break-after: always;"></div>

## 🐱 [http.cat](https://http.cat)

Vous pouvez visualiser les codes HTTP de manière amusante avec [http.cat](https://http.cat), leurs descriptions associées et des images de chats :

![418](https://http.cat/418.jpg)

<br>

## **📌 <u>À retenir</u>**

* Les **codes HTTP décrivent le résultat d’une requête**
* Ils aident à savoir rapidement **si l’action a réussi ou échoué**, et pourquoi
* Savoir les utiliser = clé pour écrire une API propre et compréhensible
