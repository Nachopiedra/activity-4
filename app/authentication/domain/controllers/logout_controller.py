from app.authentication.domain.persistences.token_interface import TokenInterface


class LogoutController:
    """Use case: close a user session by invalidating its token."""

    def __init__(self, token_persistence: TokenInterface) -> None:
        self._token_persistence = token_persistence

    def logout(self, token: str) -> None:
        self._token_persistence.delete_token(token)

