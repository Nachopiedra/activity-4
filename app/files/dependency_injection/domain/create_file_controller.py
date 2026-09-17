from app.files.dependency_injection.auth_client import auth_client
from app.files.dependency_injection.persistences.file_bo_persistences import (
    file_persistence,
)
from app.files.domain.controllers.create_file_controller import CreateFileController

create_file_controller = CreateFileController(
    auth_client=auth_client,
    file_persistence=file_persistence,
)
