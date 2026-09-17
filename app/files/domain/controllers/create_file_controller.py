from app.files.domain.auth_client import AuthClient
from app.files.domain.bo.file_bo import FileBO
from app.files.domain.persistences.file_bo_interface import FileInterface


class CreateFileController:
    """Use case: create new file metadata for the authenticated user."""

    def __init__(self, auth_client: AuthClient, file_persistence: FileInterface) -> None:
        self._auth_client = auth_client
        self._file_persistence = file_persistence

    async def create_file(self, token: str, title: str, author: str) -> FileBO:
        user = await self._auth_client.introspect(token)
        return self._file_persistence.create_file(
            owner_username=user.username, title=title, author=author
        )
