import os
from typing import List, Optional

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    auth_token: str
    cors_origin: Optional[List[str]] = Field(None)
    db_url : str


settings = Settings(
    _env_file=f".env.{os.getenv('DEMO_RUN_MODE')}",
    _env_file_encoding='utf-8'
)
