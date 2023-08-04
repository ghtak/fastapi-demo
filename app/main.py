import asyncio
import logging

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse, JSONResponse

from app.core.container import Container
from app.core.settings import settings
from app.entities.base import init_models
from app.internal.logging_middleware import logging_middleware_impl
from app.routes.router import router


class AppInitializer:
    def __init__(self):
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)

        self.app = FastAPI()
        self.container = Container.instance()
        self.container.config.from_dict(settings.dict())

        self.apply_cors()

        self.app.include_router(router)
        # self.app.include_router(v1_routes, prefix='/api')
        # self.app.include_router(v2_routes, prefix='/api')

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

asyncio.create_task(init_models())


@app.get("/")
async def root():
    return RedirectResponse(url='/index', status_code=302)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": f"Oops! {exc} did something. There goes a rainbow..."},
    )


@app.exception_handler(RequestValidationError)
async def global_exception_handler0(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"message": f"Oops! {exc} did something. There goes a rainbow..."},
    )

# @app.middleware('http')
# async def logging_middleware(request: Request, call_next):
#     return await logging_middleware_impl(request, call_next)
