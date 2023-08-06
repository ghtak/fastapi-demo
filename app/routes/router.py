from fastapi import APIRouter

from app.routes.samples.router import router as sample_router
from app.routes.api.v1.router import router as v1_router
from app.routes.api.v2.router import router as v2_router

router = APIRouter()
routers = [sample_router,
           v1_router, v2_router]

for r in routers:
    # r.tags = router.tags.append("xx")
    router.include_router(r)
