from typing import Optional, List

from pydantic import BaseModel, Field

from app.dtos.common import PagingBase


class UserDto(BaseModel):
    id: int
    name: str


class UserUpdateDto(BaseModel):
    id: int
    name: str = Field('', examples='name')


class UserCreateDto(BaseModel):
    name: str = Field(..., examples='name')


class PagingUserDtos(PagingBase):
    items: Optional[List[UserDto]]
