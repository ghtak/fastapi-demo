from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession


async def get_session() -> AsyncIterator[AsyncSession]:
    from app.main import container
    async with container.async_sessionmaker().begin() as session:
        yield session


# class DBSession:
#     def __init__(self, async_sessionmaker):
#         self.async_sessionmaker = async_sessionmaker
#
#     async def __call__(self, *args, **kwargs):
#         async with self.async_sessionmaker.begin() as session:
#             yield session
#
#
# def db_session_func(async_sessionmaker):
#     async def impl():
#         async with async_sessionmaker().begin() as session:
#             yield session
#     return impl

# async def db_session(async_sessionmaker) -> AsyncIterator[AsyncSession]:
#     async with async_sessionmaker().begin() as session:
#         yield session
#
# '''
# if inspect.isasyncgenfunction(get_session)
#     cm = asynccontextmanager(get_session)()
#     cls = type(cm)
#     _enter = cls.__aenter__
#     _exit = cls.__aexit__
#     session: AsyncSession = await _enter(cm)
#     await _exit(cm, None, None, None)
# '''
#
#
# @inject
# async def db_session(session=Depends(Provide[Container.async_sessionmaker])) -> AsyncIterator[AsyncSession]:
#     async with session() as s:
#         yield s
#
#
# print(inspect.CO_ASYNC_GENERATOR,
#       inspect.CO_COROUTINE,
#       inspect.CO_GENERATOR,
#       inspect.CO_ITERABLE_COROUTINE,
#       inspect.CO_NESTED,
#       inspect.CO_NEWLOCALS,
#       inspect.CO_NOFREE,
#       inspect.CO_OPTIMIZED,
#       inspect.CO_VARARGS,
#       inspect.CO_VARKEYWORDS)
#
# import dis
#
# for x in [db_session, get_session]:
#     print(x, inspect.isasyncgen(x))
#     print(x, inspect.isasyncgenfunction(x))
#     print(x, inspect.isawaitable(x))
#     print(x, inspect.iscoroutine(x))
#
#     dis.show_code(x)


# @inject
# async def db_session0(async_sessionmaker=Depends(Provide[Container.async_sessionmaker])):
#     session: AsyncSession = async_sessionmaker()
#     try:
#         yield session
#     except Exception:
#         await session.rollback()
#         raise
#     finally:
#         await session.close()
