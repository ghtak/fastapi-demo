from fastapi import APIRouter

from app.routes.samples.index import router as index_router
from app.routes.samples.response_sample import router as r_router
from app.routes.samples.dependencies import router as d_router
from app.routes.samples.http_basic import router as h_router
from app.routes.samples.path import router as p_router

router = APIRouter(prefix="/samples")
routers = [index_router,
           r_router, d_router, h_router,p_router]

for r in routers:
    # r.tags = router.tags.append("xx")
    router.include_router(r)
