from typing import Optional
from urllib.parse import urlparse

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = Field(default=None, env='DATABASE_URL')

    REDIS_URL: Optional[str] = Field(default=None, env="REDIS_URL")
    REDIS_HOST: Optional[str] = Field(default=None, env="REDIS_URL")
    REDIS_PORT: Optional[str] = Field(default=None, env="REDIS_URL")

    TG_BOT_TOKEN: str = Field(default=None, env='TG_BOT_TOKEN')

    DEBUG: bool = Field(default=False, env='DEBUG')

    @field_validator("REDIS_HOST")
    def validator_redis_host(cls, v):
        return urlparse(v).hostname

    @field_validator("REDIS_PORT")
    def validator_redis_port(cls, v):
        return urlparse(v).port


settings = Settings()
