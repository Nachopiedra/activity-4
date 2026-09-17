from app.files.domain.controllers.get_file_controller import GetFileController
from app.files.dependency_injection.auth_client import auth_client
from app.files.dependency_injection.persistences.file_bo_persistences import (
    file_persistence,
)

get_file_controller = GetFileController(
    auth_client=auth_client,
    file_persistence=file_persistence,
)
