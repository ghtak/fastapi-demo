import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    AUTH_TOKEN: str


settings = Settings(
    _env_file=f".env.{os.getenv('DEMO_RUN_MODE')}",
    _env_file_encoding='utf-8'
)
