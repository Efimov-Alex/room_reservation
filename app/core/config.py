# app/core/config.py
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    app_description: str = 'Сделано с fastApi'
    database_url: str

    class Config:
        env_file = '.env'


settings = Settings() 