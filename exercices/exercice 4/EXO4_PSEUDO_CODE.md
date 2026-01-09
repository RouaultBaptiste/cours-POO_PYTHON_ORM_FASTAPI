# Exercice 4 - Partie 1 : Pseudo-code cycle de session SQLModel

## Étapes pour gérer la persistance des données avec SQLModel

### 1. Créer l'engine de connexion à la base de données
```
# Importer les modules nécessaires
from sqlmodel import create_engine
from conf.settings import DATABASE_URL

# Créer l'engine de connexion
engine = create_engine(DATABASE_URL)

# Créer les tables dans la base de données
sqlmodel.metadata.create_all(engine)
```

### 2. Ouvrir une session SQLModel
```
# Importer Session
from sqlmodel import Session

# Créer une session locale
with Session(engine) as session:
    # La session est automatiquement fermée à la fin
    # Toutes les opérations BDD se font ici
```

### 3. Récupérer tous les utilisateurs
```
# Importer le modèle User
from models.user import User

# Créer la requête SQL
statement = select(User)

# Exécuter la requête
resultats = session.exec(statement)

# Récupérer les résultats dans une liste
utilisateurs = resultats.all()

# Convertir en liste Python
liste_users = list(utilisateurs)
```

### 4. Cycle complet avec gestion d'erreurs
```
try:
    # Étape 1 : Créer l'engine
    engine = create_engine(DATABASE_URL)
    
    # Étape 2 : Créer les tables
    sqlmodel.metadata.create_all(engine)
    
    # Étape 3 : Ouvrir la session
    with Session(engine) as session:
        
        # Étape 4 : Exécuter la requête
        statement = select(User)
        resultats = session.exec(statement)
        
        # Étape 5 : Récupérer les résultats
        utilisateurs = resultats.all()
        
        # Étape 6 : Traiter les données
        for user in utilisateurs:
            print(f"Utilisateur: {user.full_name}")
            
except Exception as e:
    # Gérer les erreurs de connexion
    print(f"Erreur BDD: {e}")
finally:
    # La session est automatiquement fermée par le with
    print("Session fermée correctement")
```

### Résumé du cycle
1. **Création engine** → Connexion à la BDD
2. **Création tables** → Structure BDD
3. **Ouverture session** → Contexte de travail
4. **Exécution requête** → Dialogue avec BDD
5. **Récupération résultats** → Données exploitables
6. **Fermeture session** → Nettoyage ressources
