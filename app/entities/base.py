from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


async def init_models():
    from app.core.container import Container
    async with Container.instance().database().engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
