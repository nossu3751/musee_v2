#DEFINING SCHEMA
from typing import Dict, List
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class RoleBase(BaseModel):
    id: int
    role_name: str