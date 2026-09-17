import os
import uuid

from pypdf import PdfMerger

from app.files.domain.auth_client import AuthClient
from app.files.domain.bo.file_bo import FileBO
from app.files.domain.persistences.exceptions import (
    FileContentNotFoundException,
    UnauthorizedException,
)
from app.files.domain.persistences.file_bo_interface import FileInterface
from app.files.domain.persistences.file_storage_interface import FileStorageInterface


class MergeController:
    """Use case: merge several owned PDF files into a new one."""

    def __init__(
        self,
        auth_client: AuthClient,
        file_persistence: FileInterface,
        file_storage: FileStorageInterface,
    ) -> None:
        self._auth_client = auth_client
        self._file_persistence = file_persistence
        self._file_storage = file_storage

    async def merge(self, token: str, file_ids: list[int]) -> FileBO:
        user = await self._auth_client.introspect(token)

        downloaded_paths: list[str] = []
        merged_path = f"/tmp/{uuid.uuid4()}.pdf"
        try:
            for file_id in file_ids:
                file = self._file_persistence.get_file(file_id)
                if file.owner_username != user.username:
                    raise UnauthorizedException()
                if not file.has_content or file.object_name is None:
                    raise FileContentNotFoundException()
                local_path = await self._file_storage.get_file(
                    file.object_name, "/tmp"
                )
                downloaded_paths.append(local_path)

            merger = PdfMerger()
            for path in downloaded_paths:
                merger.append(path)
            merger.write(merged_path)
            merger.close()

            merged_meta = self._file_persistence.create_file(
                owner_username=user.username,
                title="merged",
                author=user.username,
            )
            object_name = f"{uuid.uuid4()}.pdf"
            await self._file_storage.put_file(merged_path, object_name)
            merged_meta.object_name = object_name
            merged_meta.has_content = True
            self._file_persistence.update_file(merged_meta)
            return merged_meta
        finally:
            for path in downloaded_paths:
                if os.path.exists(path):
                    os.remove(path)
            if os.path.exists(merged_path):
                os.remove(merged_path)
