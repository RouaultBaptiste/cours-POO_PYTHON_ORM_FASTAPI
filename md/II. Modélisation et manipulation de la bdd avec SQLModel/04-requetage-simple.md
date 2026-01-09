![logo-digi](../img/logo-diginamic.png)

<br>

# **Requêtage simple avec SQLModel**

<br>

## **<u>Sommaire</u>**

- [**Requêtage simple avec SQLModel**](#requêtage-simple-avec-sqlmodel)
  - [**Sommaire**](#sommaire)
  - [**Sessions avec SQLModel**](#sessions-avec-sqlmodel)
    - [**Pourquoi utiliser `with` ?**](#pourquoi-utiliser-with-)
    - [**Et après une modification ?**](#et-après-une-modification-)
  - [**Introduction aux opérations CRUD**](#introduction-aux-opérations-crud)
    - [**Exemple de modèle utilisé**](#exemple-de-modèle-utilisé)
    - [**Créer un enregistrement**](#créer-un-enregistrement)
    - [**Lire des enregistrements**](#lire-des-enregistrements)
    - [**Mettre à jour un enregistrement**](#mettre-à-jour-un-enregistrement)
    - [**Supprimer un enregistrement**](#supprimer-un-enregistrement)

<div style="page-break-after: always;"></div>

## **<u>Sessions avec SQLModel</u>**

Pour lire ou écrire dans la base, on utilise une **session** :

```python
from sqlmodel import Session

with Session(engine) as session:
    # écrire ou lire ici
    ...
```

### **Pourquoi utiliser `with` ?**

* Gère automatiquement l'ouverture et la fermeture de la connexion
* Évite les erreurs de fuite de session
* Permet un code plus propre et robuste

### **Et après une modification ?**

```python
session.commit()
```

* Nécessaire pour **valider** les insertions, mises à jour ou suppressions
* Sans `commit()`, les données ne sont **pas enregistrées**

<br>

## **<u>Introduction aux opérations CRUD</u>**

On parle d’opérations **CRUD** pour désigner :

| Terme      | Action                       |
| ---------- | ---------------------------- |
| **Create** | Créer une nouvelle ligne     |
| **Read**   | Lire une ou plusieurs lignes |
| **Update** | Modifier une ligne existante |
| **Delete** | Supprimer une ligne          |

### **Exemple de modèle utilisé**

```python
class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
```

<div style="page-break-after: always;"></div>

### **Créer un enregistrement**

```python
new_hero = Hero(name="Superman", secret_name="Clark Kent")

with Session(engine) as session:
    session.add(new_hero)
    session.commit()
```

<br>

### **Lire des enregistrements**

```python
from sqlmodel import select

with Session(engine) as session:
    statement = select(Hero).where(Hero.name == "Superman")
    result = session.exec(statement).first()
    print(result)
```

* `.first()` → renvoie le premier résultat ou `None`
* `.one()` → renvoie exactement un résultat ou lève une exception si aucun ou plusieurs résultats
* `.all()` → renvoie une **liste de tous les résultats**

<br>

### **Mettre à jour un enregistrement**

```python
with Session(engine) as session:
    hero = session.get(Hero, 1)
    hero.name = "Batman"
    session.add(hero)
    session.commit()
```

> ⚠️ On utilise `session.add(...)` même pour une mise à jour

<br>

### **Supprimer un enregistrement**

```python
with Session(engine) as session:
    hero = session.get(Hero, 1)
    session.delete(hero)
    session.commit()
```
