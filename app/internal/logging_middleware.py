import logging

from fastapi import Request, Response
from starlette.types import Message


async def set_body(request: Request, body: bytes):
    async def receive() -> Message:
        return {'type': 'http.request', 'body': body}

    request._receive = receive


async def logging_middleware_impl(request: Request, call_next):
    request_body = await request.body()
    await set_body(request, request_body)
    response = await call_next(request)
    response_body = b""
    async for chunk in response.body_iterator:
        response_body += chunk
    return Response(content=response_body, status_code=response.status_code,
                    headers=dict(response.headers), media_type=response.media_type)
