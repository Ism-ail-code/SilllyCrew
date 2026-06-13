from collections.abc import AsyncGenerator
import uuid
from venv import create

from sqlalchemy import Column,String,Text,DateTime,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Relationship
DATABASEURL="sqlite_aiosqlite:///.test.db"

class post (DeclarativeBase):
    __tablename__ = "Posts"
    id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
