# /app/models.py
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.ext.declarative import declarative_base
from typing import List

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    role_name = Column(String(30), nullable=False)
    items = relationship("Item", back_populates="seller", uselist=True) #uselist: indicates one to many by making it a list

class Item(Base):
    __tablename__="items"

    id=Column(Integer, primary_key=True, index=True)
    seller_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    seller = relationship("User", back_populates="items")
    item_name = Column(String(150), nullable=False)
    price = Column(Numeric, nullable=False)