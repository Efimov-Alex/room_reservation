"""app/models/meeting_room.py."""

from sqlalchemy import Column, String, Text

from core.db import Base


class MeetingRoom(Base):
    """Модель комнаты."""

    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
