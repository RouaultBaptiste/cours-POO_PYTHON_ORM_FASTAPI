# Gestion des sessions SQLModel
from sqlmodel import create_engine, Session, SQLModel
from conf.settings import settings

# Créer l'engine de connexion à la base de données
# L'engine gère le pool de connexions et la communication avec la BDD
engine = create_engine(settings.database_url)

def create_db_and_tables():
    """
    Crée toutes les tables définies dans les modèles SQLModel
    À appeler au démarrage de l'application
    """
    SQLModel.metadata.create_all(engine)

def get_session():
    """
    Crée et retourne une session SQLModel
    Utiliser avec 'with' pour gestion automatique de la fermeture
    """
    with Session(engine) as session:
        yield session

# Fonction utilitaire pour créer une session manuellement
def create_session():
    """
    Crée une session SQLModel manuelle
    Nécessite fermeture manuelle : session.close()
    """
    return Session(engine)
