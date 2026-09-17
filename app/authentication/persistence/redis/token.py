import uuid

import redis

from app.authentication.domain.persistences.exceptions import TokenNotFound
from app.authentication.domain.persistences.token_interface import TokenInterface


class RedisTokenPersistence(TokenInterface):
    """Redis-backed adapter for session tokens.

    Tokens are stored as ``token -> username`` pairs with a TTL, so sessions
    expire automatically and the service can scale to several workers.
    """

    def __init__(self, host: str, port: int, expiration_seconds: int) -> None:
        self._client = redis.Redis(host=host, port=port, db=0, decode_responses=True)
        self._expiration_seconds = expiration_seconds

    def generate_token(self, username: str) -> str:
        token = str(uuid.uuid4())
        while self._client.exists(token):
            token = str(uuid.uuid4())
        self._client.setex(token, self._expiration_seconds, username)
        return token

    def get_username(self, token: str) -> str:
        username = self._client.get(token)
        if username is None:
            raise TokenNotFound()
        return username

    def delete_token(self, token: str) -> None:
        deleted = self._client.delete(token)
        if deleted == 0:
            raise TokenNotFound()
