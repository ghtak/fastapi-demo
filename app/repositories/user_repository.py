from typing import Callable

from sqlalchemy.ext.asyncio import AsyncSession

from app.entities.user import User


class UserRepository:
    def __init__(self, async_sessionmaker : Callable[..., AsyncSession]):
        self.async_sessionmaker = async_sessionmaker

    async def create(self, user: User):
        async with self.async_sessionmaker() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user