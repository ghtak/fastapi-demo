from __future__ import annotations

from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.repositories.user_repository import UserRepository
from app.usecases.user.user_usecase import UserUsecase


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    wiring_config = containers.WiringConfiguration(
        modules=[
            # 'app.core.db_session',
            # 'app.routes.index',
            'app.routes.api.v1.user',
        ])

    # AsyncEngine
    engine = providers.Singleton(
        create_async_engine,
        url=config.db_url,
        echo=True
    )

    async_sessionmaker = providers.Singleton(
        async_sessionmaker,
        bind=engine,
        expire_on_commit=False
    )

    user_repository = providers.Singleton(
        UserRepository, async_sessionmaker=async_sessionmaker)

    user_usecase = providers.Singleton(
        UserUsecase, user_repository=user_repository)
    #
    # db_session = providers.Singleton(
    #     db_session_func,
    #     async_sessionmaker=async_sessionmaker
    # )
