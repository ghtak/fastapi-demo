from fastapi import APIRouter
from app.routes.api.v1.user import router as user_router


router = APIRouter(prefix='/api/v1')
routers = [user_router]

for r in routers:
    # r.tags = router.tags.append("xx")
    router.include_router(r)
