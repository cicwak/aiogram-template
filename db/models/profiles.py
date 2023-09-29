from contextvars import ContextVar

from db.models.base import ModelBase
from sqlalchemy import Column, BigInteger, String


class Profiles(ModelBase):
    __tablename__ = "profiles"

    tg_id = Column(BigInteger, unique=True, index=True, nullable=False)
    nickname = Column(String)
    full_name = Column(String)


profile_session_var: ContextVar[Profiles] = ContextVar("profile_session_var")
