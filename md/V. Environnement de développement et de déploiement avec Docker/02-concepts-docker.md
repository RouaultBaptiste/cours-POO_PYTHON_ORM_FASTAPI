
![logo-diginamic](../img/logo-diginamic.png)

<br>

# **🧠 Concepts clés de Docker**

<br>

## **<u>Sommaire</u>**

* [Image](#image)
* [Container](#container)
* [Dockerfile](#dockerfile)
* [Volumes](#volumes)
* [Réseaux Docker](#réseaux-docker)
* [Variables d’environnement](#variables-denvironnement)

<div style="page-break-after: always;"></div>

## **<u>Image</u>**

* 🎯 **But** : Définir un environnement logiciel complet (OS, dépendances, code…)
* 💡 **Explication** : Une image est un **modèle figé** que Docker peut exécuter.
* ✅ **Exemple** :

  ```Dockerfile
  FROM python:3.11
  ```

<br>

## **<u>Container</u>**

* 🎯 **But** : Exécuter l’application dans un environnement isolé
* 💡 **Explication** : Un container est une **image qui tourne**. Il est temporaire et autonome.
* ✅ **Exemple** :

  ```bash
  docker run python:3.11 python --version
  ```

<br>

## **<u>Dockerfile</u>**

* 🎯 **But** : Automatiser la création d’une image
* 💡 **Explication** : Le Dockerfile est un **script de construction** d’image.
* ✅ **Exemple** :

  ```Dockerfile
  FROM python:3.11
  COPY . /app
  RUN pip install -r /app/requirements.txt
  CMD ["python", "/app/main.py"]
  ```

<div style="page-break-after: always;"></div>

## **<u>Volumes</u>**

* 🎯 **But** : Conserver les données même si le container est supprimé
* 💡 **Explication** : Les volumes sont **liés à l’hôte** et permettent de sauvegarder ou partager des fichiers.
* ✅ **Exemple** :

  ```bash
  docker run -v /data:/app/data my-image
  ```

<br>

## **<u>Réseaux Docker</u>**

* 🎯 **But** : Permettre aux containers de se **parler entre eux**
* 💡 **Explication** : Docker crée des réseaux virtuels pour connecter les containers ensemble.
* ✅ **Exemple** :

  ```yaml
  services:
    api:
      networks: [backend]
    db:
      networks: [backend]
  ```

<br>

## **<u>Variables d’environnement</u>**

* 🎯 **But** : Configurer dynamiquement une application
* 💡 **Explication** : Ces variables sont passées au container au lancement.
* ✅ **Exemple** :

  ```yaml
  environment:
    - ENV=production
  ```
