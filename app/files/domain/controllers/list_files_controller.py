from app.files.domain.auth_client import AuthClient
from app.files.domain.bo.file_bo import FileBO
from app.files.domain.persistences.file_bo_interface import FileInterface


class ListFilesController:
    """Use case: list all files owned by the authenticated user."""

    def __init__(self, auth_client: AuthClient, file_persistence: FileInterface) -> None:
        self._auth_client = auth_client
        self._file_persistence = file_persistence

    async def list_files(self, token: str) -> list[FileBO]:
        user = await self._auth_client.introspect(token)
        return self._file_persistence.list_files(user.username)
