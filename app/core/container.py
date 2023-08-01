from typing import Optional

from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    wiring_config = containers.WiringConfiguration(
        modules=[
            'app.api.v1.index.endpoint'
        ]
    )