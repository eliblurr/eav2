from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str
    API_BASE_URL: str
    COMPANY_URL: str
    STATIC_DIR: str = None
    MISFIRE_GRACE_TIME: int = 60
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: str
    MAIL_SERVER: str
    MAIL_FROM_NAME: str
    MAIL_TLS: bool
    MAIL_SSL: bool
    USER_CREDENTIALS: bool
    SECRET_KEY: str
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()

# env settings are read once ie. first time they are read
@lru_cache()
def get_settings():
    return Settings()