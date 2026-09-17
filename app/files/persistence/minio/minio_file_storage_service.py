from minio import Minio

from app.files.domain.persistences.file_storage_interface import FileStorageInterface


class MinioFileStorageService(FileStorageInterface):
    """MinIO/S3 adapter for file-content persistence."""

    def __init__(
        self,
        endpoint: str,
        access_key: str,
        secret_key: str,
        bucket: str,
        secure: bool = False,
    ) -> None:
        self._client = Minio(
            endpoint,
            access_key=access_key,
            secret_key=secret_key,
            secure=secure,
        )
        self._bucket = bucket

    async def put_file(self, local_path: str, remote_identifier: str) -> None:
        self._client.fput_object(self._bucket, remote_identifier, local_path)

    async def get_file(self, remote_identifier: str, local_folder: str) -> str:
        local_path = f"{local_folder}/{remote_identifier}"
        self._client.fget_object(self._bucket, remote_identifier, local_path)
        return local_path

    async def remove_file(self, remote_identifier: str) -> None:
        self._client.remove_object(self._bucket, remote_identifier)
