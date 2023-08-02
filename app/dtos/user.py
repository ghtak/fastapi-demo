from typing import Optional, List

from pydantic import BaseModel

from app.dtos.common import PagingBase


class UserDto(BaseModel):
    id: int
    name: str


class UserCreateDto(BaseModel):
    name: str


class PagingUserDtos(PagingBase):
    items: Optional[List[UserDto]]
