import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "05008"
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_NAME: str = "blogs_db"

    @property
    def database_url(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
settings = Settings()
