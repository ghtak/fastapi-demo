from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from pydantic.main import BaseModel
from pydantic.v1.main import ModelMetaclass
from sqlalchemy import CursorResult
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.v1.index.dto import IndexPost
from app.core.container import Container
from app.core.database import get_session, Database

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
        #db: Database = Depends(Provide[Container.database]),
        session: AsyncSession = Depends(get_session)
) -> str:
    from sqlalchemy.sql import text
    # async with db.async_session() as session:
    #     cursor : CursorResult = await session.execute(
    #         text('select * from asset_hub_assets')
    #     )
    #     for c in cursor:
    #         print(c)

    cursor : CursorResult = await session.execute(
        text('select * from asset_hub_assets')
    )
    for c in cursor:
        print(c)
    return f"hello fastapi-demo {token} {session}"


@router.post('/')
async def index_post(idx_post: IndexPost):
    return idx_post.name
