from fastapi import APIRouter


router = APIRouter(prefix='/api/v2')
routers = []

for r in routers:
    # r.tags = router.tags.append("xx")
    router.include_router(r)
