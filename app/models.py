from sqlalchemy import Column
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import Integer, String

from app.db import Base
from app.schemas import UserLevel


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    age = Column(Integer, nullable=True)
    level = Column(SQLEnum(UserLevel), default=UserLevel.beginner)
    hashed_password = Column(String)

