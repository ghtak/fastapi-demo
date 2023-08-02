from dependency_injector.wiring import inject
from fastapi import APIRouter

router = APIRouter(prefix='/index', tags=['index'])


@router.get('/')
@inject
async def index() -> str:
    return f"hello fastapi-demo"
