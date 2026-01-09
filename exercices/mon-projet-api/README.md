# API Projet - Exercice 2

## Description
API FastAPI développée dans le cadre de l'exercice 2 du cours POO Python ORM FastAPI.

## Structure du projet
```
mon-projet-api/
├── src/              # code source de l'application 
│   ├── main.py       # point d'entrée de l'application 
│   ├── models/       # models et schémas SQLModel 
│   ├── repositories/ # logique de manipulation des models 
│   ├── services/     # logique métier 
│   ├── routes/       # endpoints FastAPI 
│   ├── conf/         # gestion de la configuration 
│   └── utils/        # fonctions utilitaires 
├── tests/ 
│   ├── conftest.py   # configuration des tests unitaires 
│   └── test_*.py     # tests unitaires 
├── .env              # variables d'environnement   
├── requirements.txt  # liste des dépendances 
└── README.md         # documentation du projet
```

## Installation
1. Créer et activer un environnement virtuel :
```bash
python -m venv venv
venv\Scripts\activate
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

## Lancement de l'application
```bash
uvicorn src.main:app --reload
```

## Endpoints disponibles
- `GET /health` - Vérification de santé de l'API

## Documentation
- Interface Swagger : http://localhost:8000/docs
- Documentation ReDoc : http://localhost:8000/redoc