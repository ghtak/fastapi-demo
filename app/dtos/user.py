from typing import Optional, List

from pydantic import BaseModel, Field

from app.dtos.common import PagingBase


class UserDto(BaseModel):
    id: int
    name: str


class UserUpdateDto(BaseModel):
    id: int
    name: str = Field('', exclude='name')


class UserCreateDto(BaseModel):
    name: str = Field(..., exclude='name')

class PagingUserDtos(PagingBase):
    items: Optional[List[UserDto]]
