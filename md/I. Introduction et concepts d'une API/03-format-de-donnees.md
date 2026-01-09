![logo diginamic](../img/logo-diginamic.png)

<br>

# **Formats de données dans les API**

<br>

## **<u>Sommaire</u>**

- [**Formats de données dans les API**](#formats-de-données-dans-les-api)
  - [**Sommaire**](#sommaire)
  - [**Pourquoi parler de formats de données ?**](#pourquoi-parler-de-formats-de-données-)
  - [**JSON – JavaScript Object Notation**](#json--javascript-object-notation)
    - [**📦 Exemple JSON**](#-exemple-json)
    - [**✅ Avantages**](#-avantages)
  - [**XML – eXtensible Markup Language**](#xml--extensible-markup-language)
    - [**🧾 Exemple XML**](#-exemple-xml)
    - [**❌ Inconvénients**](#-inconvénients)
  - [⚖️ **JSON vs XML – Comparatif rapide**](#️-json-vs-xml--comparatif-rapide)
  - [🎯 **Pourquoi JSON est préféré aujourd’hui ?**](#-pourquoi-json-est-préféré-aujourdhui-)

<br>

## **<u>Pourquoi parler de formats de données ?</u>**

Quand une API répond à une requête, elle renvoie **des données structurées**. Ces données doivent être :

* Compréhensibles par le client (navigateur, application, script…)
* Transmissibles via HTTP (texte)
* Faciles à lire et à manipuler dans différents langages

👉 D’où l’importance du **format d’échange** utilisé : il structure la réponse que l’on reçoit / envoie.

<div style="page-break-after: always;"></div>

## **<u>JSON – JavaScript Object Notation</u>**

Le format **JSON** est devenu **le standard des APIs modernes**. Il est :

* **Simple**, **lisible**, et **léger**
* Nativement pris en charge par JavaScript, Python, Go, etc.
* Parfait pour les échanges web et mobile

### **📦 Exemple JSON**

```json
{
  "id": 1,
  "name": "Alice",
  "email": "alice@example.com"
}
```

### **✅ Avantages**

* Facile à comprendre et manipuler
* Compatible avec la plupart des langages modernes
* Parfaitement adapté aux structures d’objets (comme en POO)

<br>

## **<u>XML – eXtensible Markup Language</u>**

Avant l’avènement de JSON, **XML** était le format dominant, notamment dans les **APIs SOAP** ou les systèmes d’entreprise.

### **🧾 Exemple XML**

```xml
<user>
  <id>1</id>
  <name>Alice</name>
  <email>alice@example.com</email>
</user>
```

### **❌ Inconvénients**

* Plus **verbeux**
* Moins lisible rapidement
* Nécessite souvent un **schéma de validation** (XSD)
* Manipulation plus lourde dans de nombreux langages

<div style="page-break-after: always;"></div>

## ⚖️ **<u>JSON vs XML – Comparatif rapide</u>**

| Critère       | JSON                            | XML                               |
| ------------- | ------------------------------- | --------------------------------- |
| Lisibilité    | ✅ Simple, naturel               | ❌ Plus verbeux                    |
| Taille        | ✅ Compact                       | ❌ Plus lourd                      |
| Support natif | ✅ Navigateurs, JS, Python, etc. | ❌ Moins direct, nécessite parsers |
| Validation    | ⚠️ Moins structuré              | ✅ Très strict avec schémas        |
| Utilisation   | APIs REST, modernes             | APIs SOAP, anciens systèmes       |

<br>

## 🎯 **<u>Pourquoi JSON est préféré aujourd’hui ?</u>**

* **Compact**, donc plus rapide à envoyer / recevoir
* **Lisible et modifiable** facilement
* Pris en charge **nativement** dans tous les navigateurs et outils modernes
* Très adapté au modèle **clé/valeur** utilisé dans les objets métiers

> ✅ **Dans ce cours**, nous utiliserons **uniquement JSON** dans les requêtes et réponses API.