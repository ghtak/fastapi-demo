from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from pydantic.main import BaseModel
from pydantic.v1.main import ModelMetaclass

from app.api.v1.index.dto import IndexPost
from app.core.container import Container

# router = APIRouter(prefix='/index', route_class=LoggingAPIRoute)
router = APIRouter(prefix='/index', tags=['index'])


class Base(BaseModel):
    ...


class X(ModelMetaclass):
    ...


@router.get('/')
@inject
async def index(
        token: str = Depends(Provide[Container.config.AUTH_TOKEN])
) -> str:
    return f"hello fastapi-demo {token}"


@router.post('/')
async def index_post(idx_post: IndexPost):
    return idx_post.name
