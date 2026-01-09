![logo-digi](../img/logo-diginamic.png)

<br>

# **Requêtage Many-to-Many avec SQLModel**

Une relation **many-to-many** permet à :

* un héros d'appartenir à **plusieurs équipes**,
* une équipe de contenir **plusieurs héros**.

Contrairement aux relations One-to-Many, cela nécessite une **table de liaison intermédiaire**, également appelée *link table*.

<br>

## **<u>Sommaire</u>**

- [**Requêtage Many-to-Many avec SQLModel**](#requêtage-many-to-many-avec-sqlmodel)
  - [**Sommaire**](#sommaire)
  - [**Définir une relation many-to-many**](#définir-une-relation-many-to-many)
    - [**Déclaration des modèles**](#déclaration-des-modèles)
    - [🔍 Détails importants :](#-détails-importants-)
  - [**Création avec plusieurs liens**](#création-avec-plusieurs-liens)
  - [**Ajout d’un lien Many-to-Many**](#ajout-dun-lien-many-to-many)
  - [**Suppression d’un lien Many-to-Many**](#suppression-dun-lien-many-to-many)

<div style="page-break-after: always;"></div>

## **<u>Définir une relation many-to-many</u>**

<br>

### **Déclaration des modèles**

> Table de liaison : `HeroTeamLink`

```python
class HeroTeamLink(SQLModel, table=True):
    team_id: int | None = Field(default=None, foreign_key="team.id", primary_key=True)
    hero_id: int | None = Field(default=None, foreign_key="hero.id", primary_key=True)
```

> Table de données : `Team`

```python
class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    heroes: list["Hero"] = Relationship(back_populates="teams", link_model=HeroTeamLink)
```

> Table de données : `Hero`

```python
class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)

    teams: list[Team] = Relationship(back_populates="heroes", link_model=HeroTeamLink)
```

### 🔍 Détails importants :

* `HeroTeamLink` contient **deux clés étrangères**, définies comme **clé primaire combinée**.
* Les champs `heroes` et `teams` permettent une navigation **dans les deux sens**.
* Le paramètre `link_model=HeroTeamLink` indique le modèle utilisé pour faire le lien.

<div style="page-break-after: always;"></div>

## **<u>Création avec plusieurs liens</u>**

```python
team_preventers = Team(name="Preventers", headquarters="Sharp Tower")
team_z_force = Team(name="Z-Force", headquarters="Sister Margaret's Bar")

hero_deadpond = Hero(name="Deadpond", secret_name="Dive Wilson", teams=[team_z_force, team_preventers])
hero_rusty_man = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48, teams=[team_preventers])
hero_spider_boy = Hero(name="Spider-Boy", secret_name="Pedro Parqueador", teams=[team_preventers])

session.add(hero_deadpond)
session.add(hero_rusty_man)
session.add(hero_spider_boy)
session.commit()
```

> 💡 Ici, chaque héros peut être ajouté à plusieurs équipes **en une seule instruction**.

<br>

## **<u>Ajout d’un lien Many-to-Many</u>**

```python
hero_spider_boy = session.exec(select(Hero).where(Hero.name == "Spider-Boy")).one()
team_z_force = session.exec(select(Team).where(Team.name == "Z-Force")).one()

team_z_force.heroes.append(hero_spider_boy)
session.add(team_z_force)
session.commit()
```

> ⚠️ Ce n’est **pas une mise à jour d’objet**, mais bien un **ajout de lien** dans la table de liaison.

<br>

## **<u>Suppression d’un lien Many-to-Many</u>**

```python
hero_spider_boy.teams.remove(team_z_force)
session.add(team_z_force)
session.commit()
```

> Contrairement au One-to-Many, on **ne supprime pas l'objet**. On **retire la relation** entre les deux entités.
> On peut aussi utiliser `session.delete(team_z_force)` pour supprimer l'équipe, mais cela entraînerait la suppression de tous les liens associés dans `HeroTeamLink`.
