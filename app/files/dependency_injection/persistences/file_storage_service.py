from app.config import minio_settings
from app.files.persistence.minio.minio_file_storage_service import (
    MinioFileStorageService,
)

file_storage_service = MinioFileStorageService(
    endpoint=minio_settings.endpoint,
    access_key=minio_settings.access_key,
    secret_key=minio_settings.secret_key,
    bucket=minio_settings.bucket,
    secure=minio_settings.secure,
)
