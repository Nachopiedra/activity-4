from app.authentication.domain.bo.user_bo import UserBO
from app.authentication.domain.persistences.exceptions import (
    UsernameAlreadyTakenException,
    UserNotFoundException,
)
from app.authentication.domain.persistences.user_bo_interface import UserInterface


class MemoryUserPersistence(UserInterface):
    """In-memory adapter for user persistence, backed by a dictionary."""

    def __init__(self) -> None:
        self._users: dict[str, UserBO] = {}

    def create_user(self, user: UserBO) -> None:
        if user.username in self._users:
            raise UsernameAlreadyTakenException()
        self._users[user.username] = user

    def get_user(self, username: str) -> UserBO:
        user = self._users.get(username)
        if user is None:
            raise UserNotFoundException()
        return user
