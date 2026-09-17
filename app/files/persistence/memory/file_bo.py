from app.files.domain.bo.file_bo import FileBO
from app.files.domain.persistences.exceptions import FileNotFoundException
from app.files.domain.persistences.file_bo_interface import FileInterface


class MemoryFilePersistence(FileInterface):
    """In-memory adapter for file-metadata persistence, backed by a dictionary."""

    def __init__(self) -> None:
        self._files: dict[int, FileBO] = {}
        self._id_counter = 0

    def create_file(self, owner_username: str, title: str, author: str) -> FileBO:
        file = FileBO(
            id=self._id_counter,
            owner_username=owner_username,
            title=title,
            author=author,
        )
        self._files[self._id_counter] = file
        self._id_counter += 1
        return file

    def get_file(self, file_id: int) -> FileBO:
        file = self._files.get(file_id)
        if file is None:
            raise FileNotFoundException()
        return file

    def list_files(self, owner_username: str) -> list[FileBO]:
        return [file for file in self._files.values() if file.owner_username == owner_username]

    def update_file(self, file: FileBO) -> None:
        if file.id not in self._files:
            raise FileNotFoundException()
        self._files[file.id] = file

    def delete_file(self, file_id: int) -> None:
        if file_id not in self._files:
            raise FileNotFoundException()
        del self._files[file_id]
