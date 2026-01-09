from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import EmailStr
from datetime import datetime

class UserBase(SQLModel):
    email: EmailStr = Field(index=True, unique=True)
    full_name: str = Field(min_length=1, max_length=100)
    age: Optional[int] = Field(gt=0, le=150)
    is_active: bool = Field(default=True)

class UserCreate(UserBase):
    password: str = Field(min_length=8)

class UserPatch(SQLModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    age: Optional[int] = Field(default=None, gt=0, le=150)
    is_active: Optional[bool] = None
    password: Optional[str] = Field(default=None, min_length=8)

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class UserGet(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
