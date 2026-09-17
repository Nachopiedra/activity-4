from app.files.domain.controllers.upload_content_controller import (
    UploadContentController,
)
from app.files.dependency_injection.auth_client import auth_client
from app.files.dependency_injection.persistences.file_bo_persistences import (
    file_persistence,
)
from app.files.dependency_injection.persistences.file_storage_service import (
    file_storage_service,
)

upload_content_controller = UploadContentController(
    auth_client=auth_client,
    file_persistence=file_persistence,
    file_storage=file_storage_service,
)
