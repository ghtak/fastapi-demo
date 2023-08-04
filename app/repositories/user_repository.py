from typing import Callable

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.entities.user import User


class UserRepository:
    def __init__(self, session):
        self.session = session

    async def create(self, user: User) -> User:
        async with self.session() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user

    async def update(self, user: User):
        async with self.session() as session:
            await session.merge(user)
            await session.commit()
            return user

    async def find_all(self):
        async with self.session() as session:
            result = await session.execute(select(User))
            return result.scalars().all()

    async def find_by_id(self, uid: int):
        async with self.session() as session:
            result = await session.execute(
                select(User).where(User.id == uid))
            return result.scalars().first()
