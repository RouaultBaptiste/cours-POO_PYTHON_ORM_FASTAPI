![logo-diginamic](../img/logo-diginamic.png)

<br>

# **🔧 Orchestration avec `docker-compose`**

<br>

## **<u>Sommaire</u>**

- [**Orchestration avec `docker-compose`**](#orchestration-avec-docker-compose)
  - [**Objectif**](#objectif)
  - [**Qu’est-ce qu’un service ?**](#quest-ce-quun-service-)
  - [**Variables d’environnement**](#variables-denvironnement)
  - [**Exemple : API + base de données PostgreSQL**](#exemple-api--base-de-données-postgresql)
  - [**Commandes utiles**](#commandes-utiles)

<div style="page-break-after: always;"></div>

## **<u>Objectif</u>**

Gérer plusieurs **services (API, base de données, etc.)** dans un **fichier unique** : `docker-compose.yml`.

<br>

## **<u>Qu’est-ce qu’un service ?</u>**

Un **service** représente un container Docker avec sa configuration :

* image ou build
* ports à exposer
* variables d’environnement
* volumes
* dépendances éventuelles (`depends_on`)

<br>

## **<u>Variables d’environnement</u>**

Deux types :

* **Variables prédéfinies** (ex: `POSTGRES_USER`, `POSTGRES_DB`, etc.)
* **Variables personnalisées** (ex: `DATABASE_URL`, `APP_MODE`, etc.)

Elles permettent de configurer le comportement des services **sans modifier le code**.

<div style="page-break-after: always;"></div>

## **<u>Exemple : API + base de données PostgreSQL</u>**

```yaml
version: "3.8"

services:
  api:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    depends_on:
      - db
    environment:
      DATABASE_URL: postgresql://user:password@db:5432/dbname

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: dbname
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

<br>

## **<u>Commandes utiles</u>**

```bash
docker-compose up --build   # Lancer les services
docker-compose down -v      # Arrêter et supprimer les containers + volumes
```
