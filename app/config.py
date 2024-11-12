from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, PostgresDsn, validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    
    SOL_PRIVATE_KEY_HEX: str

    SOLANA_RPC_URL_ENDPOINT: str = "https://solanalb-rpc.xdefi.services"

    
    class Config:
        case_sensitive = True
        env_file_encoding = 'utf-8'
        env_file = ".env"


settings = Settings()  # type: ignore
