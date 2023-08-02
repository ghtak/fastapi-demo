from app.dtos.user import UserCreateDto, UserDto
from app.entities.user import User
from app.repositories.user_repository import UserRepository


class UserCreateUsecase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create(self, user_create_dto: UserCreateDto):
        user: User = await self.user_repository.create(
            User(name=user_create_dto.name))
        return UserDto(
            id=user.id,
            name=user.name
        )
