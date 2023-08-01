from __future__ import annotations

from typing import Optional
from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import Database
from app.core.singleton_instance import SingletonInstance


class Container(containers.DeclarativeContainer, SingletonInstance):
    config = providers.Configuration()

    wiring_config = containers.WiringConfiguration(
        modules=[
            'app.api.v1.index.endpoint',
        ])

    database = providers.Singleton(Database,
                                   db_url=config.db_url)
