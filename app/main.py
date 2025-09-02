# app/main.py
from fastapi import FastAPI

from api.meeting_room import router
from core.config import settings

app = FastAPI(title=settings.app_title)

# Подключаем роутер.
app.include_router(router)