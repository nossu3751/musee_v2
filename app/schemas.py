#DEFINING SCHEMA
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str


class USer(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
