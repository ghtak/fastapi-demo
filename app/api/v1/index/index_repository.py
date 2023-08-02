from typing import Callable

from sqlalchemy import CursorResult
from sqlalchemy.ext.asyncio import AsyncSession


class IndexRepository:
    def __init__(self, async_sessionmaker : Callable[..., AsyncSession]):
        self.async_sessionmaker = async_sessionmaker

    async def test(self):
        async with self.async_sessionmaker() as session:
            from sqlalchemy.sql import text
            cursor: CursorResult = await session.execute(
                text('select * from asset_hub_assets')
            )
            for c in cursor:
                print(c)