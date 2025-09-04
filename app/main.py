"""Файл app main.py."""
# app/main.py
from fastapi import FastAPI

# Импортируем главный роутер.
from api.routers import main_router
from core.config import settings

app = FastAPI(title=settings.app_title)

# Подключаем главный роутер.
app.include_router(main_router)
