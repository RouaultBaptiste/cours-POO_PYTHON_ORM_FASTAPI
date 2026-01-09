import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from routes.user_routes import router as user_router
from conf.session import create_db_and_tables
from repositories.user_repository import create_user_repository

app = FastAPI(title="API Projet", description="API FastAPI pour exo Baptiste Rouault", version="1.0.0")

app.include_router(user_router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.on_event("startup")
async def startup_event():
    """
    Événement au démarrage de l'application
    Crée les tables dans la base de données
    """
    create_db_and_tables()
    print("Base de données initialisée")

@app.on_event("startup")
async def test_repository():
    """
    Test du repository pour vérifier que tout fonctionne
    """
    from models.user import UserCreate
    
    repo = create_user_repository()
    
    try:
        # Test de création d'utilisateur
        user_data = UserCreate(
            email="test@example.com",
            full_name="Test User",
            age=25,
            is_active=True
        )
        
        created_user = repo.create_user(user_data)
        print(f"Utilisateur créé : {created_user.full_name} (ID: {created_user.id})")
        
        # Test de récupération
        users = repo.get_all_users()
        print(f"Nombre d'utilisateurs : {len(users)}")
        
    except Exception as e:
        print(f"Erreur lors du test : {e}")
    finally:
        repo.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)