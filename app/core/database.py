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
        self.async_session = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
        )


