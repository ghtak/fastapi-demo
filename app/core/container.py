from __future__ import annotations

from dependency_injector import containers, providers

from app.core.database import Database, SessionScope
from app.core.singleton_instance import SingletonInstance
from app.repositories.user_repository import UserRepository

from app.usecases.user.user_usecase import UserUsecase


class Container(containers.DeclarativeContainer, SingletonInstance):
    config = providers.Configuration()

    wiring_config = containers.WiringConfiguration(
        modules=[
            'app.routes.index',
            'app.routes.api.v1.user',
        ])

    database = providers.Singleton(Database, db_url=config.db_url)

    scoped_session = providers.Callable(
        SessionScope,
        db=database
    )

    user_repository = providers.Singleton(
        UserRepository, session=database.provided.session)

    user_usecase = providers.Singleton(
        UserUsecase, user_repository=user_repository)

