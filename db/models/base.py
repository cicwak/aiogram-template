from db.database import Base
from sqlalchemy import Column, Integer, DateTime, func


class ModelBase(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
