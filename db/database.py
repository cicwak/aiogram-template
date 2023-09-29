from contextlib import contextmanager
from contextvars import ContextVar
from functools import wraps
from typing import Callable, Any, Coroutine, ParamSpec, TypeVar, cast

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

SessionLocal = sessionmaker(  # type: ignore
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,  # type: ignore
)


Base = declarative_base()
P = ParamSpec("P")
T = TypeVar("T")


def require_session():
    session = db_session_var.get()
    assert session is not None, "Session context is not provided"
    return session


def transaction():
    def wrapper(
            cb: Callable[P, Coroutine[Any, Any, T]]
    ) -> Callable[P, Coroutine[Any, Any, T]]:
        @wraps(cb)
        async def wrapped(*args: P.args, **kwargs: P.kwargs) -> T:
            if db_session_var.get() is not None:
                return await cb(*args, **kwargs)

            async with cast(AsyncSession, SessionLocal()) as session:
                with use_context_value(db_session_var, session):
                    result = await cb(*args, **kwargs)
                    await session.commit()
                    return result

        return wrapped

    return wrapper


@contextmanager
def use_context_value(context: ContextVar[T], value: T):
    reset = context.set(value)
    try:
        yield
    finally:
        context.reset(reset)


db_session_var: ContextVar[AsyncSession | None] = ContextVar("db_session_var", default=None)
