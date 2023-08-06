import secrets
from enum import Enum
from typing import Any, Annotated

from dependency_injector.wiring import inject
from fastapi import APIRouter, Response, Depends, HTTPException
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from starlette import status
from starlette.responses import RedirectResponse, HTMLResponse, PlainTextResponse, StreamingResponse, FileResponse, \
    JSONResponse

router = APIRouter(prefix='/path', tags=['path'])

'''
If the parameter is also declared in the path, 
it will be used as a path parameter.
If the parameter is of a singular type (like int, float, str, bool, etc) 
it will be interpreted as a query parameter.
If the parameter is declared to be of the type of a Pydantic model, 
it will be interpreted as a request body.
'''


@router.get("/{item_id}")
def read_item(item_id):
    return {"item_id": item_id}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@router.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name}
    return {"model_name": model_name}


@router.get("/files/{file_path:path}")
async def get_file(file_path: str):
    return file_path
