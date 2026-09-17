from abc import ABC, abstractmethod


class TokenInterface(ABC):
    """Port for session-token persistence.

    Concrete adapters (e.g. Redis, in-memory) implement this contract so the
    authentication domain never depends on a specific storage technology.
    """

    @abstractmethod
    def generate_token(self, username: str) -> str:
        """Create a new session token bound to ``username`` and store it.

        Returns the generated token. Implementations must guarantee token
        uniqueness and are responsible for setting an expiration (TTL).
        """
        raise NotImplementedError

    @abstractmethod
    def get_username(self, token: str) -> str:
        """Return the username bound to ``token``.

        Raises:
            TokenNotFound: if the token does not exist or has expired.
        """
        raise NotImplementedError

    @abstractmethod
    def delete_token(self, token: str) -> None:
        """Invalidate ``token`` (close the session).

        Raises:
            TokenNotFound: if the token does not exist or has expired.
        """
        raise NotImplementedError
