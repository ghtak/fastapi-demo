import logging

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from app.core.container import Container
from app.core.settings import settings
from app.routes.router import router


class AppInitializer:
    def __init__(self):
        logging.basicConfig()
        logging.getLogger().setLevel(logging.INFO)

        self.app = FastAPI()
        self.container = Container()
        self.container.config.from_dict(settings.dict())
        # self.container.wire(
        #     modules=[
        #         'app.routes.index',
        #         'app.routes.api.v1.user',
        #     ]
        # )
        self.apply_cors()
        self.except_handlers()
        self.app.include_router(router)

    def apply_cors(self):
        if self.container.config.cors_origin():
            self.app.add_middleware(
                CORSMiddleware,
                allow_origins=self.container.config.cors_origin(),
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )

    def except_handlers(self):
        # @app.exception_handler(Exception)
        async def global_exception_handler(request: Request, exc: Exception):
            return JSONResponse(
                status_code=500,
                content={"message": f"Oops! {exc} did something. There goes a rainbow..."},
            )

        # @app.exception_handler(RequestValidationError)
        async def validation_exception_handler(request: Request, exc: RequestValidationError):
            return JSONResponse(
                status_code=422,
                content={"message": f"Oops! {exc} did something. There goes a rainbow..."},
            )

        self.app.add_exception_handler(Exception, global_exception_handler)
        self.app.add_exception_handler(RequestValidationError, validation_exception_handler)

    def apps(self):
        return self.app, self.container

    # @app.middleware('http')
    # async def logging_middleware(request: Request, call_next):
    #     return await logging_middleware_impl(request, call_next)
