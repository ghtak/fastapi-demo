from fastapi import APIRouter

from app.api.v1.index.endpoint import router as index_router


routes: APIRouter = APIRouter(prefix='/v1')
routers = [index_router]

for router in routers:
    # router.tags = routes.tags.append("v1")
    routes.include_router(router)






