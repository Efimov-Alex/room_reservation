"""app/crud/meeting_room.py."""
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.db import AsyncSessionLocal
from models.meeting_room import MeetingRoom
from schemas.meeting_room import MeetingRoomCreate, MeetingRoomUpdate
from fastapi.encoders import jsonable_encoder


async def create_meeting_room(
        new_room: MeetingRoomCreate,
        session: AsyncSession,
) -> MeetingRoom:
    """Создание новой комнаты."""
    new_room_data = new_room.dict()
    db_room = MeetingRoom(**new_room_data)
    session.add(db_room)
    await session.commit()
    await session.refresh(db_room)
    return db_room


async def get_room_id_by_name(
        room_name: str,
        session: AsyncSession,
) -> Optional[int]:
    """Получение id по имени."""
    db_room_id = await session.execute(
        select(MeetingRoom.id).where(
            MeetingRoom.name == room_name
        )
    )
    db_room_id = db_room_id.scalars().first()
    return db_room_id


async def read_all_rooms_from_db(
        session: AsyncSession,
) -> list[MeetingRoom]:
    """Получение всех комнат."""
    query = select(MeetingRoom)
    result = await session.execute(query)
    rooms = result.scalars().all()
    return rooms


async def get_meeting_room_by_id(
        room_id: int,
        session: AsyncSession,
) -> Optional[MeetingRoom]:
    """Получение комнат по id."""
    db_room = await session.execute(
        select(MeetingRoom).where(
            MeetingRoom.id == room_id
        )
    )
    db_room = db_room.scalars().first()
    return db_room


async def update_meeting_room(
        db_room: MeetingRoom,
        room_in: MeetingRoomUpdate,
        session: AsyncSession,
) -> MeetingRoom:
    """Обновление объекта."""
    obj_data = jsonable_encoder(db_room)
    update_data = room_in.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(db_room, field, update_data[field])

    session.add(db_room)
    await session.commit()
    await session.refresh(db_room)
    return db_room


async def delete_meeting_room(
        db_room: MeetingRoom,
        session: AsyncSession,
) -> MeetingRoom:
    """Удаление объекта."""
    await session.delete(db_room)
    await session.commit()
    return db_room
