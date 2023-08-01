from fastapi import APIRouter
from app.api.v2.hello.endpoint import router as hello_router


routes = APIRouter(prefix='/v2')

routers = [hello_router]

for router in routers:
    # router.tags = routes.tags.append("v2")
    routes.include_router(router)



