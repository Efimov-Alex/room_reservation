"""app/schemas/meeting_room.py."""

from typing import Optional

from pydantic import BaseModel, validator, Field


class MeetingRoomBase(BaseModel):
    """Базовый класс."""

    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]


class MeetingRoomCreate(MeetingRoomBase):
    """Создание объекта."""

    name: str = Field(..., min_length=1, max_length=100)


class MeetingRoomUpdate(MeetingRoomBase):
    """Обновление объекта."""

    @validator('name')
    def name_cannot_be_null(cls, value):
        """Валидация имени."""
        if value is None:
            raise ValueError('Имя переговорки не может быть пустым!')
        return value


class MeetingRoomDB(MeetingRoomCreate):
    """Резульатат."""

    id: int

    class Config:
        """Класс конфиг."""

        orm_mode = True
