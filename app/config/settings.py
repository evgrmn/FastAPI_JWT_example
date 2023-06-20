from __future__ import annotations

from pydantic import BaseSettings


class Settings(BaseSettings):
    ACCESS_TOKEN_EXPIRE_MILLISECONDS: int
    JWT_SECRET: str

    class Config:
        env_file = "./.env"


env = Settings()
