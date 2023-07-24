import typing
from urllib.parse import urlparse

from pydantic import BaseSettings, Field, validator


class Settings(BaseSettings):
    DATABASE_URL: str = Field(default=None, env='DATABASE_URL')

    REDIS_URL: typing.Optional[str] = Field(default=None, env="REDIS_URL")
    REDIS_HOST: typing.Optional[str] = Field(default=None, env="REDIS_URL")
    REDIS_PORT: typing.Optional[str] = Field(default=None, env="REDIS_URL")

    TG_BOT_TOKEN: str = Field(default="", env='TG_BOT_TOKEN')

    DEBUG: bool = Field(default=False, env='DEBUG')

    @validator("DEBUG")
    def validator_database_url(cls, v) -> bool:
        return v == "True"

    @validator("REDIS_HOST")
    def validator_redis_host(cls, v):
        return urlparse(v).hostname

    @validator("REDIS_PORT")
    def validator_redis_port(cls, v):
        return urlparse(v).port

    class Config:
        env_file = ".env"


settings = Settings()
