from app.files.dependency_injection.auth_client import auth_client
from app.files.dependency_injection.persistences.file_bo_persistences import (
    file_persistence,
)
from app.files.domain.controllers.list_files_controller import ListFilesController

list_files_controller = ListFilesController(
    auth_client=auth_client,
    file_persistence=file_persistence,
)
