from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from pydantic.main import BaseModel
from pydantic.v1.main import ModelMetaclass

from app.api.v1.index.index_dto import IndexPost
from app.api.v1.index.index_repository import IndexRepository
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
        token: str = Depends(Provide[Container.config.auth_token]),
        #session: AsyncSession = Depends(get_session),
        repo: IndexRepository = Depends(Provide[Container.index_repository])
) -> str:
    # from sqlalchemy.sql import text
    # cursor : CursorResult = await session.execute(
    #     text('select * from axum_demo_user')
    # )
    # for c in cursor:
    #     print(c)
    # return f"hello fastapi-demo {token} {session}"
    await repo.test()
    return f"hello fastapi-demo {token}"


@router.post('/')
async def index_post(idx_post: IndexPost):
    return idx_post.name
