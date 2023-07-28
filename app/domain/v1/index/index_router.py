from fastapi import APIRouter

from app.domain.v1.index.indexdto import IndexPost
from app.internal.logging_api_route import LoggingAPIRoute

index_router = APIRouter(route_class=LoggingAPIRoute)


@index_router.get('/', tags=['index'])
async def index():
    return "hello fastapi-demo"


@index_router.post('/')
async def index_post(index_post: IndexPost):
    return index_post.name
