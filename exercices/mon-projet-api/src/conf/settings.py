# Configuration de l'application
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """
    Gère toutes les variables de configuration de l'application
    Charge automatiquement depuis le fichier .env
    """
    # Base de données
    database_url: str = "sqlite:///./database.db"  # BDD SQLite par défaut
    
    # Application
    app_name: str = "API Projet"
    app_version: str = "1.0.0"
    debug: bool = False
    
    # Sécurité
    secret_key: Optional[str] = None
    
    class Config:
        env_file = ".env"  # Fichier des variables d'environnement

# Instance globale des settings
settings = Settings()
