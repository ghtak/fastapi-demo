from typing import List, Optional

from app.dtos.user import UserCreateDto, UserDto, UserUpdateDto
from app.entities.user import User
from app.repositories.user_repository import UserRepository


class UserUsecase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create(self, user_create_dto: UserCreateDto) -> UserDto:
        user: User = await self.user_repository.create(
            User(name=user_create_dto.name))
        return UserDto(**user.__dict__)

    async def update(self, uid: int, user_update_dto: UserUpdateDto) -> UserDto:
        user: User = await self.user_repository.update(
            User(id=uid, name=user_update_dto.name))
        return UserDto(**user.__dict__)

    async def find_all(self) -> List[UserDto]:
        items = await self.user_repository.find_all()
        return items

    async def find_by_id(self, uid: int) -> Optional[UserDto]:
        return await self.user_repository.find_by_id(uid)
