import os
from urllib.parse import urlparse

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    DATABASE_URL: str = Field(default=None, env='DATABASE_URL')

    REDIS_URL: str = Field(default=None, env="REDIS_URL")

    TG_BOT_TOKEN: str = Field(default="", env='TG_BOT_TOKEN')

    DEBUG: bool = Field(default=False, env='DEBUG')

    class Config:
        env_file = ".env"


settings = Settings()
