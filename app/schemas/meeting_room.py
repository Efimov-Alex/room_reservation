# app/schemas/meeting_room.py

from typing import Optional
from fastapi import HTTPException

from pydantic import BaseModel, validator


class MeetingRoomCreate(BaseModel):
    name: str
    description: Optional[str]

    @validator('name')
    def validate_name(cls, value):
        # Проверка на пустую строку
        if not value.strip():
            raise ValueError("Поле name не может быть пустым")
            
        # Проверка длины строки
        if len(value) > 100:
            raise ValueError("Длина поля name не может превышать 100 символов")
            
        return value