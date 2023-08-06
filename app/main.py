from app.app_initializer import AppInitializer
from app.core.run_sync import run_sync
from app.entities.base import init_models

app, container = AppInitializer().apps()

run_sync(init_models(container.engine()))


