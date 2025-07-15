import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "yourpassword"
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_NAME: str = "yourdbname"

    @property
    def database_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

settings = Settings()
