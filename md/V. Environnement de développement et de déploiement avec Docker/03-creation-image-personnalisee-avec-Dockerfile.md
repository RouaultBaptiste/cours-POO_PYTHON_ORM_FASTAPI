![logo-diginamic](../img/logo-diginamic.png)

<br>

# **🛠️ Créer une application Python avec Dockerfile**

<br>

## **<u>Sommaire</u>**

- [**Ecrire un Dockerfile pour une app Python**](#écrire-un-dockerfile-pour-une-app-python)
  - [**Sommaire**](#sommaire)
  - [**Objectif**](#objectif)
  - [**Exemple complet**](#exemple-complet)
  - [**Étapes expliquées**](#étapes-expliquées)
  - [**Résultat attendu**](#résultat-attendu)

<div style="page-break-after: always;"></div>

## **<u>Objectif</u>**

Construire une image Docker personnalisée pour une application FastAPI.

<br>

## **<u>Exemple complet</u>**

```Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

> Pour le bien de l'exemple, on copie tous les fichiers du projet dans le container: `COPY . .`  
> 
> Par contre, il est recommandé de ne copier que les fichiers nécessaires pour éviter d'alourdir l'image et de respecter les bonnes pratiques de sécurité: Eviter de copier les fichiers sensibles comme `.env`.

<br>

## **<u>Étapes expliquées</u>**

| Instruction | Rôle                                                     |
| ----------- | -------------------------------------------------------- |
| `FROM`      | Déclare l’image de base : ici une image Python légère    |
| `WORKDIR`   | Définit le dossier de travail dans le container (`/app`) |
| `COPY`      | Copie les fichiers du projet dans le container           |
| `RUN`       | Exécute une commande, ici l’installation des dépendances |
| `CMD`       | Commande lancée par défaut à l’exécution du container    |

<br>

## **<u>Résultat attendu</u>**

Une image prête à lancer votre app FastAPI sur `http://localhost:8000`.
