import httpx

from app.files.domain.bo.user_bo import UserBO
from app.files.domain.persistences.exceptions import UnauthorizedException


class AuthClient:
    """Resolves the authenticated user by calling the authentication service."""

    def __init__(self, base_url: str) -> None:
        self._introspect_url = f"{base_url}/introspect"

    async def introspect(self, token: str) -> UserBO:
        headers = {"accept": "application/json", "auth": token}
        async with httpx.AsyncClient() as client:
            response = await client.get(self._introspect_url, headers=headers)
        if response.status_code != 200:
            raise UnauthorizedException()
        data = response.json()
        return UserBO(username=data["username"])
