![logo-diginamic](../img/logo-diginamic.png)

<br>

# **🚀 Exécuter et tester avec Docker**

<br>

## **<u>Sommaire</u>**

- [**Exécuter et tester avec Docker**](#exécuter-et-tester-avec-docker)
  - [**Objectif**](#objectif)
  - [**Étapes principales**](#étapes-principales)
  - [**Exécuter les tests (avec Pytest)**](#exécuter-les-tests-avec-pytest)
  - [**Arrêt et nettoyage**](#arrêt-et-nettoyage)

<div style="page-break-after: always;"></div>

## **<u>Étapes principales</u>**

1. **Construire et lancer les services** :

```bash
docker-compose up --build
```

2. **Accéder à l’API** :

* Interface Swagger : [http://localhost:8000/docs](http://localhost:8000/docs)

3. **Vérifier les logs** :

```bash
docker-compose logs -f
```

Assurez-vous que la connexion à la base de données fonctionne (`Connected to database`, etc.).

<br>

## **<u>Exécuter les tests (avec Pytest)</u>**

Lancer les tests à l’intérieur du container :

```bash
docker-compose run --rm api pytest
```

<br>

## **<u>Arrêt et nettoyage</u>**

```bash
docker-compose down -v
```

* `-v` : supprime aussi les **volumes** (base de données, etc.)
* Cela permet de **repartir de zéro** (utile pour tester les migrations, réinitialiser l’état...)
