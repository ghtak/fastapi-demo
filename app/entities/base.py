import asyncio

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


# class Base(AsyncAttrs, DeclarativeBase):
class Base(DeclarativeBase):
    pass


async def init_models(engine):
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


