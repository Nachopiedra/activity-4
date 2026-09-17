import os
import uuid

from app.files.domain.auth_client import AuthClient
from app.files.domain.persistences.exceptions import UnauthorizedException
from app.files.domain.persistences.file_bo_interface import FileInterface
from app.files.domain.persistences.file_storage_interface import FileStorageInterface


class UploadContentController:
    """Use case: upload the binary content of an existing file to object storage."""

    def __init__(
        self,
        auth_client: AuthClient,
        file_persistence: FileInterface,
        file_storage: FileStorageInterface,
    ) -> None:
        self._auth_client = auth_client
        self._file_persistence = file_persistence
        self._file_storage = file_storage

    async def upload_content(self, token: str, file_id: int, content: bytes) -> None:
        user = await self._auth_client.introspect(token)
        file = self._file_persistence.get_file(file_id)
        if file.owner_username != user.username:
            raise UnauthorizedException()

        object_name = f"{uuid.uuid4()}.pdf"
        local_path = f"/tmp/{object_name}"
        with open(local_path, "wb") as buffer:
            buffer.write(content)
        try:
            await self._file_storage.put_file(local_path, object_name)
        finally:
            os.remove(local_path)

        file.object_name = object_name
        file.has_content = True
        self._file_persistence.update_file(file)
