# Import des outils FastAPI
from fastapi import APIRouter, HTTPException
from typing import List
from models.user import User, UserCreate, UserPatch, UserGet
from repositories.user_repository import create_user_repository

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserGet, status_code=201)
async def create_user(user_data: UserCreate):
    repo = create_user_repository()
    
    try:
        new_user = repo.create_user(user_data)
        return UserGet.from_orm(new_user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        repo.close()

@router.get("/", response_model=List[UserGet])
async def get_all_users():
    repo = create_user_repository()
    
    try:
        users = repo.get_all_users()
        return [UserGet.from_orm(user) for user in users]
    finally:
        repo.close()

@router.get("/{user_id}", response_model=UserGet)
async def get_user(user_id: int):
    repo = create_user_repository()
    
    try:
        user = repo.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
        
        return UserGet.from_orm(user)
    finally:
        repo.close()

@router.patch("/{user_id}", response_model=UserGet)
async def update_user(user_id: int, user_data: UserPatch):
    repo = create_user_repository()
    
    try:
        updated_user = repo.update_user(user_id, user_data)
        if not updated_user:
            raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
        
        return UserGet.from_orm(updated_user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        repo.close()

@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: int):
    repo = create_user_repository()
    
    try:
        deleted = repo.delete_user(user_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    finally:
        repo.close()
