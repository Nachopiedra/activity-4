from hashlib import sha256

from app.authentication.domain.bo.user_bo import UserBO
from app.authentication.domain.persistences.user_bo_interface import UserInterface


class RegisterController:
    """Use case: register a new user."""

    def __init__(self, user_persistence: UserInterface) -> None:
        self._user_persistence = user_persistence

    def register(
        self, username: str, password: str, mail: str, age_of_birth: int
    ) -> UserBO:
        hashed_password = sha256((username + password).encode()).hexdigest()
        user = UserBO(
            username=username,
            password=hashed_password,
            mail=mail,
            age_of_birth=age_of_birth,
        )
        self._user_persistence.create_user(user)
        return user
