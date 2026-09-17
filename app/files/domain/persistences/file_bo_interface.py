from abc import ABC, abstractmethod

from app.files.domain.bo.file_bo import FileBO


class FileInterface(ABC):
    """Port for file-metadata persistence."""

    @abstractmethod
    def create_file(self, owner_username: str, title: str, author: str) -> FileBO:
        """Create and persist new file metadata, returning it with a fresh id."""
        raise NotImplementedError

    @abstractmethod
    def get_file(self, file_id: int) -> FileBO:
        """Return the metadata for ``file_id``.

        Raises:
            FileNotFoundException: if no file has that id.
        """
        raise NotImplementedError

    @abstractmethod
    def list_files(self, owner_username: str) -> list[FileBO]:
        """Return all files owned by ``owner_username``."""
        raise NotImplementedError

    @abstractmethod
    def update_file(self, file: FileBO) -> None:
        """Persist changes to an existing file's metadata."""
        raise NotImplementedError

    @abstractmethod
    def delete_file(self, file_id: int) -> None:
        """Delete the metadata for ``file_id``.

        Raises:
            FileNotFoundException: if no file has that id.
        """
        raise NotImplementedError
