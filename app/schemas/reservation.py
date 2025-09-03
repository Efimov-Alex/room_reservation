from typing import Optional
from datetime import datetime, timedelta
from pydantic import BaseModel, validator, Field, root_validator


class ReservationBase(BaseModel):
    """Базовый класс."""

    from_reserve: datetime
    to_reserve: datetime


class ReservationCreate(ReservationBase):
    """Создание объекта."""

    meetingroom_id: int


class ReservationUpdate(ReservationBase):
    """Обновление объекта."""

    @validator('from_reserve')
    def check_from_reserve_later_than_now(cls, value):
        if value <= datetime.now():
            raise ValueError(
                'Время начала бронирования '
                'не может быть меньше текущего времени'
            )
        return value

    @root_validator(skip_on_failure=True)
    def check_from_reserve_before_to_reserve(cls, values):
        if values['from_reserve'] >= values['to_reserve']:
            raise ValueError(
                'Время начала бронирования '
                'не может быть больше времени окончания'
            )
        return values


class ReservationDB(ReservationCreate):
    """Резульатат."""

    id: int
    meetingroom_id: int

    class Config:
        """Класс конфиг."""

        orm_mode = True
