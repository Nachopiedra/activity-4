from app.files.domain.auth_client import AuthClient
from app.files.domain.bo.file_bo import FileBO
from app.files.domain.persistences.exceptions import UnauthorizedException
from app.files.domain.persistences.file_bo_interface import FileInterface


class GetFileController:
    """Use case: get a single file's metadata, if owned by the user."""

    def __init__(self, auth_client: AuthClient, file_persistence: FileInterface) -> None:
        self._auth_client = auth_client
        self._file_persistence = file_persistence

    async def get_file(self, token: str, file_id: int) -> FileBO:
        user = await self._auth_client.introspect(token)
        file = self._file_persistence.get_file(file_id)
        if file.owner_username != user.username:
            raise UnauthorizedException()
        return file
