from typing import List, Optional, Annotated

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.container import Container
from app.core.db_session import get_session
from app.dtos.common import Paging
from app.dtos.user import UserDto, UserCreateDto, UserUpdateDto
from app.usecases.user.user_usecase import UserUsecase

router = APIRouter(prefix='/user', tags=['index'])


@router.get('/',
            response_model=Paging[UserDto],
            summary="Get Users")
@inject
async def get_users(
        session: Annotated[AsyncSession, Depends(get_session)],
        user_usecase: UserUsecase = Depends(Provide[Container.user_usecase]),
):
    items: List[UserDto] = await user_usecase.find_all()
    return {
        'total': len(items),
        'page': 1,
        'items':
            items
    }


@router.get('/{user_id:int}')
@inject
async def get_user_by_id(
        user_id: int,
        user_usecase: UserUsecase = Depends(Provide[Container.user_usecase]),
        # user_usecase: Annotated[UserUsecase, Depends(Provide[Container.user_usecase])],
) -> Optional[UserDto]:  # response_model= or return
    user: Optional[UserDto] = await user_usecase.find_by_id(user_id)
    return user


@router.post('/')
@inject
async def create_user(
        user_create_dto: UserCreateDto,
        user_usecase: UserUsecase = Depends(Provide[Container.user_usecase]),
        # user_usecase: Annotated[UserUsecase, Depends(Provide[Container.user_usecase])],
) -> UserDto:
    return await user_usecase.create(user_create_dto)


@router.patch('/{user_id:int}', response_model=Optional[UserDto])
@inject
async def update_user(
        user_id: int,
        user_update_dto: UserUpdateDto,
        user_usecase: UserUsecase = Depends(Provide[Container.user_usecase]),
        # user_usecase: Annotated[UserUsecase, Depends(Provide[Container.user_usecase])],
):
    user_dto: UserDto = await user_usecase.update(user_id, user_update_dto)
    return user_dto
