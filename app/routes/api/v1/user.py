from typing import List

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.dtos.user import UserDto, PagingUserDtos, UserCreateDto
from app.repositories.user_repository import UserRepository
from app.usecases.user.user_create_usecase import UserCreateUsecase

router = APIRouter(prefix='/user', tags=['index'])


@router.get('/', response_model=PagingUserDtos)
@inject
async def get_users(
        user_repository: UserRepository = Depends(Provide[Container.user_repository])
):
    return {
        'total': 1,
        'page': 1,
        'items':
            [
                UserDto(id=0, name="name")
            ]
    }


@router.post('/', response_model=UserDto)
@inject
async def create_user(
        user_create: UserCreateDto,
        # user_repository: UserRepository = Depends(Provide[Container.user_repository])
        user_create_usecase: UserCreateUsecase = Depends(Provide[Container.user_create_usecase])
):
    user_dto: UserDto = await user_create_usecase.create(user_create)
    return user_dto
