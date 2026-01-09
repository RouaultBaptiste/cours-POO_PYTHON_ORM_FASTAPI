# Repository pour la gestion des utilisateurs en base de données
from sqlmodel import Session, select, delete
from typing import List, Optional
from models.user import User, UserCreate, UserPatch, UserGet
from conf.session import engine

class UserRepository:
    """
    Gère toutes les opérations CRUD pour le modèle User
    Sépare la logique métier de l'accès aux données
    """
    
    def __init__(self):
        # Crée une session pour ce repository
        self.session = Session(engine)
    
    def create_user(self, user_data: UserCreate) -> User:
        """
        Crée un nouvel utilisateur dans la base de données
        Retourne l'utilisateur créé avec son ID
        """
        # Vérifie si l'email existe déjà
        existing_user = self.get_user_by_email(user_data.email)
        if existing_user:
            raise ValueError("Email déjà utilisé")
        
        # Crée l'objet User à partir des données
        new_user = User(
            email=user_data.email,
            full_name=user_data.full_name,
            age=user_data.age,
            is_active=user_data.is_active
        )
        
        # Sauvegarde dans la base de données
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)  # Rafraîchit pour obtenir l'ID
        
        return new_user
    
    def get_all_users(self) -> List[User]:
        """
        Récupère tous les utilisateurs de la base de données
        Retourne une liste d'objets User
        """
        # Crée la requête SQL
        statement = select(User)
        
        # Exécute la requête
        result = self.session.exec(statement)
        
        # Retourne tous les résultats
        return result.all()
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """
        Récupère un utilisateur par son ID
        Retourne None si non trouvé
        """
        # Crée la requête avec filtre sur l'ID
        statement = select(User).where(User.id == user_id)
        
        # Exécute la requête
        result = self.session.exec(statement)
        
        # Retourne le premier résultat (ou None)
        return result.first()
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """
        Récupère un utilisateur par son email
        Retourne None si non trouvé
        """
        # Crée la requête avec filtre sur l'email
        statement = select(User).where(User.email == email)
        
        # Exécute la requête
        result = self.session.exec(statement)
        
        # Retourne le premier résultat (ou None)
        return result.first()
    
    def update_user(self, user_id: int, user_data: UserPatch) -> Optional[User]:
        """
        Met à jour un utilisateur existant
        Retourne l'utilisateur mis à jour ou None si non trouvé
        """
        # Récupère l'utilisateur à modifier
        user = self.get_user_by_id(user_id)
        if not user:
            return None
        
        # Si l'email est modifié, vérifie l'unicité
        if user_data.email and user_data.email != user.email:
            existing_user = self.get_user_by_email(user_data.email)
            if existing_user:
                raise ValueError("Email déjà utilisé")
        
        # Met à jour seulement les champs fournis
        update_data = user_data.dict(exclude_unset=True)
        for field, value in update_data.items():
            if hasattr(user, field):
                setattr(user, field, value)
        
        # Sauvegarde les modifications
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        
        return user
    
    def delete_user(self, user_id: int) -> bool:
        """
        Supprime un utilisateur par son ID
        Retourne True si supprimé, False si non trouvé
        """
        # Récupère l'utilisateur à supprimer
        user = self.get_user_by_id(user_id)
        if not user:
            return False
        
        # Supprime l'utilisateur
        self.session.delete(user)
        self.session.commit()
        
        return True
    
    def close(self):
        """
        Ferme la session du repository
        À appeler manuellement quand on n'utilise pas 'with'
        """
        if self.session:
            self.session.close()

# Fonctions utilitaires pour usage rapide
def create_user_repository():
    """
    Crée une instance de UserRepository
    """
    return UserRepository()

# Exemple d'utilisation avec gestion automatique de la session
def with_user_repository(func):
    """
    Décorateur pour gérer automatiquement la session du repository
    """
    def wrapper(*args, **kwargs):
        repo = create_user_repository()
        try:
            result = func(repo, *args, **kwargs)
            return result
        finally:
            repo.close()
    return wrapper
