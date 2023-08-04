from contextlib import asynccontextmanager
from typing import AsyncIterator, Optional

from dependency_injector import resources
from dependency_injector.wiring import Provide
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self, db_url):
        self.engine = create_async_engine(
            db_url,
            echo=True,
            future=True
        )
        self.base = declarative_base()
        self.async_sessionmaker = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
        )

    @asynccontextmanager
    async def session(self):
        session: AsyncSession = self.async_sessionmaker()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


class SessionScope:

    def __init__(self, db):
        self.db = db

    async def __call__(self, *args, **kwargs) -> AsyncSession:
        async with self.db.async_sessionmaker() as session:
            yield session


class ScopedSession(resources.AsyncResource):
    def __init__(self, session):
        self.session = session

    async def init(self, *args, **kwargs) -> AsyncSession:
        s: AsyncSession = self.session()
        return s

    async def shutdown(self, resource: AsyncSession):
        await resource.close()


async def get_session() -> AsyncSession:
    from app.core.container import Container
    async with Container.instance().database().async_sessionmaker() as session:
        yield session
