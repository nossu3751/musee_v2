# HANDLING DB CONNECTIONS
import aiosqlite
import asyncio
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
import models
from typing import AsyncGenerator

DATABASE_URL = "sqlite:///./test_db.db"
engine = create_engine(DATABASE_URL)
models.Base.metadata.drop_all(engine)
models.Base.metadata.create_all(engine)

# indicating that get_db is an async generator function that yields aiosqlite.
#Connection objects and eventually returns None when it's done.
async def get_db() -> AsyncGenerator[aiosqlite.Connection, None]:
    async with aiosqlite.connect(DATABASE_URL) as db:
        yield db

