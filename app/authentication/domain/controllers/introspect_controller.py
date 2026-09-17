from app.authentication.domain.bo.user_bo import UserBO
from app.authentication.domain.persistences.token_interface import TokenInterface
from app.authentication.domain.persistences.user_bo_interface import UserInterface


class IntrospectController:
    """Use case: validate a session token and return its user."""

    def __init__(self, token_persistence: TokenInterface, user_persistence: UserInterface) -> None:
        self._token_persistence = token_persistence
        self._user_persistence = user_persistence

    def introspect(self, token: str) -> UserBO:
        username = self._token_persistence.get_username(token)
        return self._user_persistence.get_user(username)
