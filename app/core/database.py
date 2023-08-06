from contextlib import asynccontextmanager
from typing import AsyncIterator, Optional

from dependency_injector import resources
from dependency_injector.wiring import Provide
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#
# class Database:
#     def __init__(self, db_url):
#         self.engine = create_async_engine(
#             db_url,
#             echo=True,
#             future=True
#         )
#         self.base = declarative_base()
#         self.async_sessionmaker = sessionmaker(
#             bind=self.engine,
#             class_=AsyncSession,
#             autocommit=False,
#             autoflush=False,
#             expire_on_commit=False,
#         )
#
#     @asynccontextmanager
#     async def session(self):
#         session: AsyncSession = self.async_sessionmaker()
#         try:
#             yield session
#         except Exception:
#             await session.rollback()
#             raise
#         finally:
#             await session.close()


# class ScopedSession(resources.AsyncResource):
#     def __init__(self, session):
#         self.session = session
#
#     async def init(self, *args, **kwargs) -> AsyncSession:
#         s: AsyncSession = self.session()
#         return s
#
#     async def shutdown(self, resource: AsyncSession):
#         await resource.close()
#

# async def get_session() -> AsyncSession:
#     from app.core.container import Container
#     async with Container.instance().database().async_sessionmaker.begin() as session:
#         yield session

# import asyncio
#
# from sqlalchemy import Column
# from sqlalchemy import MetaData
# from sqlalchemy import select
# from sqlalchemy import String
# from sqlalchemy import Table
# from sqlalchemy.ext.asyncio import create_async_engine
#
# meta = MetaData()
# t1 = Table("t1", meta, Column("name", String(50), primary_key=True))
#
#
# async def async_main() -> None:
#     engine = create_async_engine(
#         "postgresql+asyncpg://scott:tiger@localhost/test",
#         echo=True,
#     )
#
#     async with engine.begin() as conn:
#         await conn.run_sync(meta.create_all)
#
#         await conn.execute(
#             t1.insert(), [{"name": "some name 1"}, {"name": "some name 2"}]
#         )
#
#     async with engine.connect() as conn:
#         # select a Result, which will be delivered with buffered
#         # results
#         result = await conn.execute(select(t1).where(t1.c.name == "some name 1"))
#
#         print(result.fetchall())
#
#     # for AsyncEngine created in function scope, close and
#     # clean-up pooled connections
#     await engine.dispose()
#
#
# asyncio.run(async_main())


# # https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html
# from __future__ import annotations
#
# import asyncio
# import datetime
# from typing import List
#
# from sqlalchemy import ForeignKey
# from sqlalchemy import func
# from sqlalchemy import select
# from sqlalchemy.ext.asyncio import AsyncAttrs
# from sqlalchemy.ext.asyncio import async_sessionmaker
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.ext.asyncio import create_async_engine
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column
# from sqlalchemy.orm import relationship
# from sqlalchemy.orm import selectinload
#
#
# class Base(AsyncAttrs, DeclarativeBase):
#     pass
#
#
# class A(Base):
#     __tablename__ = "a"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     data: Mapped[str]
#     create_date: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
#     bs: Mapped[List[B]] = relationship()
#
#
# class B(Base):
#     __tablename__ = "b"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     a_id: Mapped[int] = mapped_column(ForeignKey("a.id"))
#     data: Mapped[str]
#
#
# async def insert_objects(async_session: async_sessionmaker[AsyncSession]) -> None:
#     async with async_session() as session:
#         async with session.begin():
#             session.add_all(
#                 [
#                     A(bs=[B(), B()], data="a1"),
#                     A(bs=[], data="a2"),
#                     A(bs=[B(), B()], data="a3"),
#                 ]
#             )
#
#
# async def select_and_update_objects(
#         async_session: async_sessionmaker[AsyncSession],
# ) -> None:
#     async with async_session() as session:
#         stmt = select(A).options(selectinload(A.bs))
#
#         result = await session.execute(stmt)
#
#         for a1 in result.scalars():
#             print(a1)
#             print(f"created at: {a1.create_date}")
#             for b1 in a1.bs:
#                 print(b1)
#
#         result = await session.execute(select(A).order_by(A.id).limit(1))
#
#         a1 = result.scalars().one()
#
#         a1.data = "new data"
#
#         await session.commit()
#
#         # access attribute subsequent to commit; this is what
#         # expire_on_commit=False allows
#         print(a1.data)
#
#         # alternatively, AsyncAttrs may be used to access any attribute
#         # as an awaitable (new in 2.0.13)
#         for b1 in await a1.awaitable_attrs.bs:
#             print(b1)
#
#
# async def async_main() -> None:
#     engine = create_async_engine(
#         "postgresql+asyncpg://scott:tiger@localhost/test",
#         echo=True,
#     )
#
#     # async_sessionmaker: a factory for new AsyncSession objects.
#     # expire_on_commit - don't expire objects after transaction commit
#     async_session = async_sessionmaker(engine, expire_on_commit=False)
#
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#
#     await insert_objects(async_session)
#     await select_and_update_objects(async_session)
#
#     # for AsyncEngine created in function scope, close and
#     # clean-up pooled connections
#     await engine.dispose()
#
#
# asyncio.run(async_main())
