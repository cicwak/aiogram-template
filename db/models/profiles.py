from sqlalchemy import Column, Integer

from db.models.base import ModelBase


class Profiles(ModelBase):
    __tablename__ = "profiles"

    tg_id = Column(Integer, unique=True, index=True, nullable=False)
