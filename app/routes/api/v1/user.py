from typing import List, Optional

from dependency_injector.wiring import inject, Provide, Closing
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.container import Container
from app.core.database import get_session
from app.dtos.user import UserDto, PagingUserDtos, UserCreateDto, UserUpdateDto
from app.entities.user import User
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




@router.get('/s', response_model=PagingUserDtos)
@inject
async def get_users(
        user_usecase: UserUsecase = Depends(Provide[Container.user_usecase]),
        session: AsyncSession = Depends(Closing[Provide[Container.scoped_session]]),
        session0: AsyncSession = Depends(Provide[Container.database.provided.session]),
        sessions: AsyncSession = Depends(get_session)
):
    # print(session, session0, sessions)
    # async with session0() as s:
    #     print(await s.execute(select(User)))

    print(session)
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


@router.post('/')
@inject
async def create_user(
        user_create_dto: UserCreateDto,
        user_usecase: UserUsecase = Depends(Provide[Container.user_usecase])
) -> UserDto:
    return await user_usecase.create(user_create_dto)


@router.patch('/{user_id:int}', response_model=Optional[UserDto])
@inject
async def update_user(
        user_id: int,
        user_update_dto: UserUpdateDto,
        user_usecase: UserUsecase = Depends(Provide[Container.user_usecase])
):
    user_dto: UserDto = await user_usecase.update(user_id, user_update_dto)
    return user_dto
