# HANDLING DB CONNECTIONS
import aiosqlite
from fastapi import Depends

DATABASE_URL = "sqlite_async:///./test.db"

async def get_db() -> aiosqlite.Connection:
    async with aiosqlite.connect(DATABASE_URL) as db:
        yield db

