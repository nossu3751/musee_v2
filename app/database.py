# HANDLING DB CONNECTIONS
import aiosqlite
from typing import AsyncGenerator
from fastapi import Depends

DATABASE_URL = "sqlite_async:///./test.db"

# indicating that get_db is an async generator function that yields aiosqlite.
#Connection objects and eventually returns None when it's done.
async def get_db() -> AsyncGenerator[aiosqlite.Connection, None]:
    async with aiosqlite.connect(DATABASE_URL) as db:
        yield db

