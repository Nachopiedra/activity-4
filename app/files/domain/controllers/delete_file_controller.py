from app.files.domain.auth_client import AuthClient
from app.files.domain.persistences.exceptions import UnauthorizedException
from app.files.domain.persistences.file_bo_interface import FileInterface
from app.files.domain.persistences.file_storage_interface import FileStorageInterface


class DeleteFileController:
    """Use case: delete a file (metadata and its content, if any)."""

    def __init__(
        self,
        auth_client: AuthClient,
        file_persistence: FileInterface,
        file_storage: FileStorageInterface,
    ) -> None:
        self._auth_client = auth_client
        self._file_persistence = file_persistence
        self._file_storage = file_storage

    async def delete_file(self, token: str, file_id: int) -> None:
        user = await self._auth_client.introspect(token)
        file = self._file_persistence.get_file(file_id)
        if file.owner_username != user.username:
            raise UnauthorizedException()
        if file.has_content and file.object_name is not None:
            await self._file_storage.remove_file(file.object_name)
        self._file_persistence.delete_file(file_id)
