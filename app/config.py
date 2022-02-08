import os
from pydantic import BaseSettings, Field
from functools import lru_cache

os.environ["CQLENG_ALLOW_SCHEMA_MANAGEMENT"] = "1"


class Settings(BaseSettings):
    db_username: str = Field(..., env="DATABASE_USERNAME")
    db_password: str = Field(..., env="DATABASE_PASSWORD")
    db_host: str = Field(..., env="DATABASE_HOST")
    db_name: str = Field(..., env="DATABASE_NAME")
    db_port: str = Field(..., env="DATABASE_PORT")
    secret_key: str = Field(..., env="SECRET_KEY")
    algorithm: str = Field(..., env="ALGORITHM")
    access_token_expire_minutes: int = Field(...,env="ACCESS_TOKEN_EXPIRE_MINUTES")

    class Config:
        env_file = '.env'


@lru_cache
def get_settings():
    return Settings()
