from sqlalchemy.orm import Mapped, mapped_column

from app.entities.base import Base
from sqlalchemy import (
    Integer,
    String,
    Column
)


class User(Base):
    __tablename__ = 'user_table'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]

