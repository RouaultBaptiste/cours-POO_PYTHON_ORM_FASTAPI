![logo-diginamic](../img/logo-diginamic.png)

<br>

# **Introduction à FastAPI**

FastAPI est un framework moderne, rapide et efficace pour construire des API web en Python. Lancé en 2018, il s’appuie sur des technologies puissantes et récentes pour offrir à la fois simplicité, performance et robustesse.

FastAPI repose principalement sur deux bibliothèques clés :

* **Starlette** : un framework web léger et asynchrone qui gère les requêtes HTTP de manière performante
* **Pydantic** : qui fournit une validation et une sérialisation des données basée sur les annotations de type Python

<br>

## **Pourquoi choisir FastAPI ?**

* **Documentation interactive automatique**
  Dès que vous écrivez vos routes, FastAPI génère pour vous une documentation Swagger UI accessible via `/docs` et une documentation ReDoc via `/redoc`.
* **Support natif de l’asynchrone**
  FastAPI est conçu pour exploiter le paradigme `async/await` de Python, ce qui permet de gérer un grand nombre de requêtes simultanées sans blocage.
* **Validation et sérialisation automatiques**
  En s’appuyant sur Pydantic, FastAPI valide les données entrantes et formate les réponses, tout en exploitant la puissance des **type hints** Python.
* **Performances élevées**
  FastAPI se positionne parmi les frameworks web Python les plus rapides, souvent comparable à Node.js ou Go sur certains benchmarks.

<br>

### **Quelques utilisateurs connus**

FastAPI est adopté par de grandes entreprises et projets, par exemple :

* **Netflix** utilise FastAPI pour certains services internes et microservices, bénéficiant de sa rapidité et simplicité.
* **Microsoft** a également intégré FastAPI dans plusieurs projets internes.
* De nombreux projets open source et startups choisissent FastAPI pour accélérer le développement tout en gardant un code propre et maintenable.
