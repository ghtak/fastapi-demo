from app.entities.base import Base
from sqlalchemy import (
    Integer,
    String,
    Column
)


class User(Base):
    __tablename__ = 'user_table'
    id = Column(Integer,
                autoincrement=True,
                primary_key=True)
    name = Column(String)
