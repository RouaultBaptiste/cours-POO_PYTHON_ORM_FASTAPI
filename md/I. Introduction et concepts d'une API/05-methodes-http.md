![logo-diginamic](../img/logo-diginamic.png)

<br>

# 📘 **Méthodes HTTP**

<br>

## **<u>Sommaire</u>**

- [📘 **Méthodes HTTP**](#-méthodes-http)
  - [**Sommaire**](#sommaire)
  - [**🔁 Méthodes HTTP : que veut faire le client ?**](#-méthodes-http--que-veut-faire-le-client-)
  - [**✏️ Exemples détaillés**](#️-exemples-détaillés)
    - [**🔹 `GET` – Lire une ressource**](#-get--lire-une-ressource)
    - [**🔹 `POST` – Créer une ressource**](#-post--créer-une-ressource)
    - [**🔹 `PUT` – Remplacer une ressource**](#-put--remplacer-une-ressource)
    - [**🔹 `PATCH` – Modifier partiellement**](#-patch--modifier-partiellement)
    - [**🔹 `DELETE` – Supprimer une ressource**](#-delete--supprimer-une-ressource)
  - [**📌 À retenir**](#-à-retenir)

<div style="page-break-after: always;"></div>

## **🔁 <u>Méthodes HTTP : que veut faire le client ?</u>**

|  Méthode | Action                  | Exemple           | Réponses typiques                 |
| -------: | ----------------------- | ----------------- | --------------------------------- |
|    `GET` | Lire une ressource      | `GET /users/1`    | `200 OK`, `404 Not Found`         |
|   `POST` | Créer une ressource     | `POST /users`     | `201 Created`, `400 Bad Request`  |
|    `PUT` | Remplacer entièrement   | `PUT /users/1`    | `200 OK`, `204 No Content`, `404` |
|  `PATCH` | Modifier partiellement  | `PATCH /users/1`  | `200 OK`, `400`, `404`            |
| `DELETE` | Supprimer une ressource | `DELETE /users/1` | `204 No Content`, `404`           |

<br>

## **✏️ <u>Exemples détaillés</u>**

### **🔹 `GET` – Lire une ressource**

```http
GET /products/42
````

* ✅ Réponse réussie : `200 OK`
* ❌ Produit inexistant : `404 Not Found`

<br>

### **🔹 `POST` – Créer une ressource**

```http
POST /users
{
  "name": "Alice",
  "email": "alice@mail.com"
}
```

* ✅ Création réussie : `201 Created`
* ❌ Format incorrect : `400 Bad Request`

<div style="page-break-after: always;"></div>

### **🔹 `PUT` – Remplacer une ressource**

```http
PUT /users/1
{
  "name": "Bob",
  "email": "bob@mail.com"
}
```

* ✅ Succès : `200 OK` ou `204 No Content`
* ❌ Utilisateur inexistant : `404 Not Found`

<br>

### **🔹 `PATCH` – Modifier partiellement**

```http
PATCH /users/1
{
  "email": "new@mail.com"
}
```

* ✅ Succès : `200 OK`
* ❌ Erreur client : `400 Bad Request`
* ❌ Utilisateur absent : `404 Not Found`

<br>

### **🔹 `DELETE` – Supprimer une ressource**

```http
DELETE /comments/18
```

* ✅ Supprimé : `204 No Content`
* ❌ Déjà supprimé / inexistant : `404 Not Found`

<br>

## **📌 <u>À retenir</u>**

* Chaque **méthode HTTP correspond à une intention** (lire, créer, modifier, supprimer)
* Elle est toujours accompagnée d’un **code de retour pour en indiquer le résultat**
* Comprendre et bien choisir ses méthodes rend une API cohérente et prévisible
