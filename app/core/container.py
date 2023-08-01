from __future__ import annotations

from typing import Optional
from dependency_injector import containers, providers

from app.core.database import Database


class Container(containers.DeclarativeContainer):
    instance: Container = None

    @staticmethod
    def get_insatnce():
        return Container.instance

    config = providers.Configuration()

    wiring_config = containers.WiringConfiguration(
        modules=[
            'app.api.v1.index.endpoint'
        ]
    )

    database = providers.Singleton(Database,
                                   db_url=config.db_url)


container = None