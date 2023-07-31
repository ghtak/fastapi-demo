from fastapi import APIRouter

from app.internal.logging_api_route import LoggingAPIRoute

router = APIRouter(prefix='/index', route_class=LoggingAPIRoute)