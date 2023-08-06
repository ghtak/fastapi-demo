from typing import Optional, List

from pydantic import BaseModel, Field

from app.dtos.common import PagingBase, Paging


class UserDto(BaseModel):
    id: int
    name: str


class UserUpdateDto(BaseModel):
    name: str = Field('')


class UserCreateDto(BaseModel):
    name: str = Field(...)


# class PagingUserDtos(PagingBase):
#     items: Optional[List[UserDto]]

# PagingUserDtos = Paging[UserDto]