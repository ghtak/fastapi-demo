from __future__ import annotations

from dependency_injector import containers, providers

from app.core.database import Database
from app.core.singleton_instance import SingletonInstance
from app.repositories.user_repository import UserRepository
from app.usecases.user.user_create_usecase import UserCreateUsecase


class Container(containers.DeclarativeContainer, SingletonInstance):
    config = providers.Configuration()

    wiring_config = containers.WiringConfiguration(
        modules=[
            'app.routes.index',
            'app.routes.api.v1.user',
        ])

    database = providers.Singleton(Database, db_url=config.db_url)

    user_repository = providers.Singleton(
        UserRepository,
        async_sessionmaker=database.provided.async_sessionmaker
    )

    user_create_usecase = providers.Singleton(
        UserCreateUsecase,
        user_repository=user_repository
    )