# /app/main.py
import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import models, schemas, database
import aiosqlite
import asyncio
from src.auth import auth
from database import get_db
from sqlalchemy.ext.asyncio import create_async_engine

# todo save it in .env
DATABASE_URL = "sqlite+aiosqlite:////../test_db.db"

# models.Base.metadata.create_all(bind=engine())
engine = create_async_engine(DATABASE_URL)
app = FastAPI()

@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=5000, log_level="info", reload=True)