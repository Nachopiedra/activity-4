from abc import ABC, abstractmethod


class FileStorageInterface(ABC):
    """Port for file-content persistence (object storage).

    Concrete adapters (e.g. MinIO/S3) implement this contract so the files
    domain never depends on a specific object-storage technology.
    """

    @abstractmethod
    async def put_file(self, local_path: str, remote_identifier: str) -> None:
        """Upload the file at ``local_path`` to storage as ``remote_identifier``."""
        raise NotImplementedError

    @abstractmethod
    async def get_file(self, remote_identifier: str, local_folder: str) -> str:
        """Download ``remote_identifier`` into ``local_folder``.

        Returns the local path of the downloaded file.
        """
        raise NotImplementedError

    @abstractmethod
    async def remove_file(self, remote_identifier: str) -> None:
        """Delete ``remote_identifier`` from storage."""
        raise NotImplementedError
