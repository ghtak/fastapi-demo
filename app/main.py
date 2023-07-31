from fastapi import FastAPI, Request
from starlette.responses import RedirectResponse

from app.domain.v1.index import router

import logging

from app.internal.logging_middleware import logging_middleware_impl

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

app = FastAPI()

# app.include_router(app.domain.v1.index.router , prefix='/index')


@app.get("/")
async def root():
    return RedirectResponse(url='/index', status_code=302)


@app.middleware('http')
async def logging_middleware(request: Request, call_next):
    return await logging_middleware_impl(request, call_next)
