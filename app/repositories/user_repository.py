from typing import Callable

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.entities.user import User


class UserRepository:
    def __init__(self, async_sessionmaker: Callable[..., AsyncSession]):
        self.async_sessionmaker = async_sessionmaker

    async def create(self, user: User) -> User:
        async with self.async_sessionmaker() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user

    async def update(self, user: User):
        async with self.async_sessionmaker() as session:
            await session.merge(user)
            await session.commit()
            return user

    async def find_all(self):
        async with self.async_sessionmaker() as session:
            result = await session.execute(select(User))
            return result.scalars().all()

    async def find_by_id(self, uid: int):
        async with self.async_sessionmaker() as session:
            result = await session.execute(
                select(User).where(User.id == uid))
            return result.scalars().first()
