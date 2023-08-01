import logging

from fastapi import FastAPI, Request
from starlette.responses import RedirectResponse

from app.api.v1.routes import routes as v1_routes
from app.api.v2.routes import routes as v2_routes
from app.core.container import Container
from app.core.settings import settings
from app.internal.logging_middleware import logging_middleware_impl
from fastapi.middleware.cors import CORSMiddleware


class AppInitializer:
    def __init__(self):
        self.app = FastAPI()
        self.container = Container()
        self.container.config.from_dict(settings.dict())
        Container.instance = self.container
        self.apply_cors()
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)

        self.app.include_router(v1_routes, prefix='/api')
        self.app.include_router(v2_routes, prefix='/api')

    def apply_cors(self):
        if self.container.config.cors_origin():
            self.app.add_middleware(
                CORSMiddleware,
                allow_origins=self.container.config.cors_origin(),
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )


app_initializer = AppInitializer()
app = app_initializer.app

@app.get("/")
async def root():
    return RedirectResponse(url='/index', status_code=302)


@app.middleware('http')
async def logging_middleware(request: Request, call_next):
    return await logging_middleware_impl(request, call_next)
