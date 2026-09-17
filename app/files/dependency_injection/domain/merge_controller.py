from app.files.domain.controllers.merge_controller import MergeController
from app.files.dependency_injection.auth_client import auth_client
from app.files.dependency_injection.persistences.file_bo_persistences import (
    file_persistence,
)
from app.files.dependency_injection.persistences.file_storage_service import (
    file_storage_service,
)

merge_controller = MergeController(
    auth_client=auth_client,
    file_persistence=file_persistence,
    file_storage=file_storage_service,
)
