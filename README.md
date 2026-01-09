# Cours POO - SQLModel - FastAPI

🎓 **Cours complet sur la Programmation Orientée Objet, SQLModel et FastAPI**

## 📋 Contenu du cours

### 🏗️ **Module I - Introduction et concepts d'une API**
- Définition et principes des APIs
- Types d'APIs (REST, SOAP, GraphQL)
- Formats de données (JSON, XML)
- Codes de retour HTTP
- Méthodes HTTP (GET, POST, PUT, DELETE, PATCH)

### 🗄️ **Module II - Modélisation et manipulation de la BDD avec SQLModel**
- Introduction à SQLModel
- Création de tables et modèles
- Mise en place de la base de données
- Requêtage simple et avancé
- Relations One-to-Many et Many-to-Many

### 🚀 **Module III - Création d'une API REST avec FastAPI**
- Introduction à FastAPI
- Définition des endpoints
- Schémas de données et validation
- Documentation automatique avec Swagger
- Injection de dépendances
- Gestion des erreurs
- Organisation du projet

### 🧪 **Module IV - Tests automatisés avec Pytest**
- Pourquoi tester ?
- Types de tests (unitaires, intégration, fonctionnels)
- Introduction à Pytest
- Tests HTTP avec HTTPX
- Fixtures et couverture de code

### 🐳 **Module V - Docker et déploiement**
- Pourquoi Docker ?
- Concepts Docker (images, containers)
- Création d'images personnalisées
- Orchestration avec Docker Compose
- Bonnes pratiques Docker

## 🎯 **Exercices pratiques**

### **Exercice 1** - Setup de l'environnement
- Installation Python et dépendances
- Configuration de l'environnement virtuel
- Structure de projet

### **Exercice 2** - MVP FastAPI
- Création d'une API minimale
- Endpoint de health check
- Documentation Swagger

### **Exercice 3** - Modèles et CRUD
- Création des modèles SQLModel
- Implémentation des routes CRUD
- Validation des données

### **Exercice 4** - SQLModel Repository Pattern
- Configuration de la base de données
- Implémentation du repository pattern
- Gestion des sessions SQLModel
- CRUD complet avec persistance

### **Exercice 5** - Authentification et Pagination
- JWT et authentification
- Gestion des permissions
- Pagination des résultats
- Filtrage et tri

## 🏃‍♂️ **Démarrage rapide**

```bash
# Cloner le repository
git clone https://github.com/RouaultBaptiste/cours-POO_PYTHON_ORM_FASTAPI.git
cd cours-POO_PYTHON_ORM_FASTAPI

# Accéder au projet API
cd exercices/mon-projet-api

# Installer les dépendances
pip install -r requirements.txt

# Démarrer l'API
uvicorn src.main:app --reload

# Accéder à la documentation
# http://localhost:8000/docs
```

## 📁 **Structure du projet**

```
cours-POO_PYTHON_ORM_FASTAPI/
├── md/                    # Cours au format Markdown
├── pdf/                   # Cours au format PDF
├── exercices/             # Exercices pratiques
│   ├── exercice 1/        # Setup environnement
│   ├── exercice 2/        # MVP FastAPI
│   ├── exercice 3/        # Modèles et CRUD
│   ├── exercice 4/        # SQLModel Repository
│   └── mon-projet-api/    # Projet final
│       ├── src/
│       │   ├── models/    # Modèles SQLModel
│       │   ├── routes/    # Routes FastAPI
│       │   ├── conf/      # Configuration
│       │   └── repositories/ # Repository pattern
│       ├── tests/         # Tests
│       └── requirements.txt
└── README.md
```

## 🛠️ **Technologies utilisées**

- **Python 3.11+** - Langage principal
- **FastAPI** - Framework API moderne
- **SQLModel** - ORM Python moderne
- **SQLite/PostgreSQL** - Base de données
- **Pydantic** - Validation de données
- **Pytest** - Tests automatisés
- **Docker** - Conteneurisation
- **Uvicorn** - Serveur ASGI

## 📚 **Ressources**

- [Documentation FastAPI](https://fastapi.tiangolo.com/)
- [Documentation SQLModel](https://sqlmodel.tiangolo.com/)
- [Documentation Pydantic](https://pydantic-docs.helpmanual.io/)
- [Documentation Pytest](https://docs.pytest.org/)

## 👨‍🏫 **Formateur**

**Baptiste Rouault**  
Développeur Python et formateur spécialisé dans les APIs modernes

---

🚀 **Prêt à maîtriser FastAPI et SQLModel ?**  
Commencez par l'exercice 1 et progressez pas à pas !
