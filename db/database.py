from contextvars import ContextVar

from core.config import settings
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")


engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_recycle=900,
    pool_size=100, max_overflow=3
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,  # type: ignore
)


Base = declarative_base()


def get_db() -> SessionLocal:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_session_var: ContextVar[AsyncSession] = ContextVar("db_session_var")
