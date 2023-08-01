from dependency_injector.wiring import Provide


async def get_session(Depends(Provide[Container.database])) -> AsyncSession:
    async with async_session() as session:
        yield session
