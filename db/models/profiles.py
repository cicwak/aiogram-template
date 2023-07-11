from contextvars import ContextVar

from sqlalchemy import Column, BigInteger

from db.models.base import ModelBase


class Profiles(ModelBase):
    __tablename__ = "profiles"

    tg_id = Column(BigInteger, unique=True, index=True, nullable=False)


profile_session_var: ContextVar[Profiles] = ContextVar("profile_session_var")
