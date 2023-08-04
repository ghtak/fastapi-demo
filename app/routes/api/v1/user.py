from typing import List, Optional

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.dtos.user import UserDto, PagingUserDtos, UserCreateDto, UserUpdateDto
from app.usecases.user.user_usecase import UserUsecase

router = APIRouter(prefix='/user', tags=['index'])


@router.get('/', response_model=PagingUserDtos)
@inject
async def get_users(
        user_usecase: UserUsecase = Depends(Provide[Container.user_usecase])
):
    items: List[UserDto] = await user_usecase.find_all()
    return {
        'total': len(items),
        'page': 1,
        'items':
            items
    }


@router.get('/{user_id:int}', response_model=Optional[UserDto])
@inject
async def get_user_by_id(
        user_id: int,
        user_usecase: UserUsecase = Depends(Provide[Container.user_usecase])
):
    user: Optional[UserDto] = await user_usecase.find_by_id(user_id)
    return user


@router.post('/', response_model=UserDto)
@inject
async def create_user(
        user_create_dto: UserCreateDto,
        user_usecase: UserUsecase = Depends(Provide[Container.user_usecase])
):
    user_dto: UserDto = await user_usecase.create(user_create_dto)
    return user_dto


@router.patch('/', response_model=UserDto)
@inject
async def update_user(
        user_update_dto: UserUpdateDto,
        user_usecase: UserUsecase = Depends(Provide[Container.user_usecase])
):
    user_dto: UserDto = await user_usecase.update(user_update_dto)
    return user_dto
