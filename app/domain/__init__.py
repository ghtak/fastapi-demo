from fastapi import APIRouter
from app.domain.v1.index import router as index_router

routers = APIRouter()
routers.include_router(index_router)