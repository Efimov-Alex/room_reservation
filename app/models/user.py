# app/models/user.py
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

# Новый импорт.
from sqlalchemy import Column, DateTime, String

from core.db import Base

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

class User(SQLAlchemyBaseUserTable[int], Base):
    pass 