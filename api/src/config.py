from pydantic_settings import BaseSettings
from functools import lru_cache
import os

class Settings(BaseSettings):
    ENV: str = "development"
    DATABASE_URL: str = "mysql+pymysql://alphasort:alphasort_password@127.0.0.1/alphasort_dev"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

class ProductionSettings(Settings):
    ENV: str = "production"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "mysql+pymysql://alphasort:alphasort_password@127.0.0.1/alphasort")
    DEBUG: bool = False

class StagingSettings(Settings):
    ENV: str = "staging"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "mysql+pymysql://alphasort:alphasort_password@127.0.0.1/alphasort_staging")
    DEBUG: bool = True

@lru_cache()
def get_settings():
    env = os.getenv("ENV", "development")
    if env == "production":
        return ProductionSettings()
    elif env == "staging":
        return StagingSettings()
    return Settings()

settings = get_settings()
