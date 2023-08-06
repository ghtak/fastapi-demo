from typing import Any

from dependency_injector.wiring import inject
from fastapi import APIRouter, Response
from starlette.responses import RedirectResponse, HTMLResponse, PlainTextResponse, StreamingResponse, FileResponse, \
    JSONResponse

router = APIRouter(prefix='/response_sample', tags=['response_sample'])


@router.get('/redirect', response_class=RedirectResponse)
async def redirect():
    return "https://google.com"


@router.get('/html', response_class=HTMLResponse)
async def html():
    html_content = """
        <html>
            <head>
                <title>Some HTML in here</title>
            </head>
            <body>
                <h1>Look ma! HTML!</h1>
            </body>
        </html>
        """
    return HTMLResponse(content=html_content, status_code=200)


@router.get('/planetext', response_class=PlainTextResponse)
async def redirect():
    return "https://google.com"


async def fake_video_streamer():
    for i in range(10):
        yield b"some fake video bytes"


@router.get('/streaming')
async def streaming():
    # def iterfile():  #
    #     with open(some_file_path, mode="rb") as file_like:  #
    #         yield from file_like  #
    #
    # return StreamingResponse(iterfile(), media_type="video/mp4")
    return StreamingResponse(fake_video_streamer())


@router.get('/file')
async def file():
    some_file_path = "large-video-file.mp4"
    return FileResponse(some_file_path)


# @router.get('/file',response_class=FileResponse)
# async def file():
#     some_file_path = "large-video-file.mp4"
#     return some_file_path


# class CustomORJSONResponse(Response):
#     media_type = "application/json"
#
#     def render(self, content: Any) -> bytes:
#         assert orjson is not None, "orjson must be installed"
#         return orjson.dumps(content, option=orjson.OPT_INDENT_2)
#
#
# @router.get('/custom', response_class=CustomORJSONResponse)
# async def custom():
#     return {"message": "Hello World"}


@router.get('/cookie')
def create_cookie():
    content = {"message": "Come to the dark side, we have cookies"}
    res: Response = JSONResponse(content=content)
    res.set_cookie(key="fakesession", value="fake-cookie-session-value")
    res.headers['xxx'] = 'yyyy'
    return res