from fastapi import APIRouter
from pydantic.v1.main import ModelMetaclass, BaseModel

from app.domain.v1.index import router
from app.domain.v1.index.dto import IndexPost
from app.internal.logging_api_route import LoggingAPIRoute


class Base(BaseModel):
    ...


class X(ModelMetaclass):
    ...


@router.get('/', tags=['index'])
async def index():
    return "hello fastapi-demo"


@router.post('/')
async def index_post(idx_post: IndexPost):
    return idx_post.name
