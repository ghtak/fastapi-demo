from dependency_injector.wiring import inject
from fastapi import APIRouter
from starlette.responses import RedirectResponse, HTMLResponse, PlainTextResponse, StreamingResponse, FileResponse

router = APIRouter(prefix='/index', tags=['index'])


@router.get('/')
@inject
async def index() -> str:
    return f"hello fastapi-demo"
