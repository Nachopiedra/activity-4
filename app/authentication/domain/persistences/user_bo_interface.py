from abc import ABC, abstractmethod

from app.authentication.domain.bo.user_bo import UserBO


class UserInterface(ABC):
    """Port for user persistence.

    Concrete adapters (in-memory, PostgreSQL, ...) implement this contract so
    the authentication domain never depends on a specific storage technology.
    """

    @abstractmethod
    def create_user(self, user: UserBO) -> None:
        """Persist a new user.

        Raises:
            UsernameAlreadyTakenException: if the username already exists.
        """
        raise NotImplementedError

    @abstractmethod
    def get_user(self, username: str) -> UserBO:
        """Return the user identified by ``username``.

        Raises:
            UserNotFoundException: if no user has that username.
        """
        raise NotImplementedError
