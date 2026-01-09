![logo-diginamic](../img/logo-diginamic.png)

<br>

# **✅ Bonnes pratiques avec Docker**

<br>

## **<u>Sommaire</u>**

- [**Bonnes pratiques avec Docker**](#bonnes-pratiques-avec-docker)
  - [**Environnements séparés**](#environnements-séparés)
  - [**Sécurité**](#sécurité)
  - [**Optimisations**](#optimisations)

<br>

## **<u>Environnements séparés</u>**

* Utiliser un fichier `docker-compose.override.yml` pour le développement local
* Créer une image de production plus légère avec un **multi-stage build**
* Séparer les variables (`.env.dev`, `.env.prod`)

<br>

## **<u>Sécurité</u>**

* Ne jamais inclure de **secrets** dans le code ou dans les images

  * Utiliser des variables d’environnement injectées au runtime
* Ajouter un fichier `.dockerignore` pour éviter d’inclure des fichiers sensibles ou inutiles (ex: `.env`, `.git`, `__pycache__`)

<br>

## **<u>Optimisations</u>**

* Partir d’**images officielles** ou maintenues (ex: `python:3.11-slim`)
* Supprimer le cache lors de l’installation des dépendances :

```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

* Minimiser le nombre d’instructions dans le `Dockerfile` pour accélérer les builds
* Ne copier que ce qui est nécessaire (`COPY requirements.txt .` avant `COPY . .`)
