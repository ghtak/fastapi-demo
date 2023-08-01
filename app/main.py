from dependency_injector.wiring import Provide
from fastapi import FastAPI, Request, Depends
from starlette.responses import RedirectResponse

from app.core.container import Container
from app.api.v1.routes import routes as v1_routes
from app.api.v2.routes import routes as v2_routes

import logging

from app.core.settings import settings
from app.internal.logging_middleware import logging_middleware_impl

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

app = FastAPI()
app.container = Container()
app.container.config.from_dict(settings.dict())


app.include_router(v1_routes, prefix='/api')
app.include_router(v2_routes, prefix='/api')


@app.get("/")
async def root():
    return RedirectResponse(url='/index', status_code=302)


@app.middleware('http')
async def logging_middleware(request: Request, call_next):
    return await logging_middleware_impl(request, call_next)
