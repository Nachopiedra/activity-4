from hashlib import sha256

from app.authentication.domain.persistences.exceptions import WrongPasswordException
from app.authentication.domain.persistences.token_interface import TokenInterface
from app.authentication.domain.persistences.user_bo_interface import UserInterface


class LoginController:
    """Use case: authenticate a user and open a session."""

    def __init__(self, user_persistence: UserInterface, token_persistence: TokenInterface) -> None:
        self._user_persistence = user_persistence
        self._token_persistence = token_persistence

    def login(self, username: str, password: str) -> str:
        user = self._user_persistence.get_user(username)
        hashed_input_password = sha256((username + password).encode()).hexdigest()
        if hashed_input_password != user.password:
            raise WrongPasswordException()
        return self._token_persistence.generate_token(username)
