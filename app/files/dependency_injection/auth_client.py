from app.config import internal_service_settings
from app.files.domain.auth_client import AuthClient

auth_client = AuthClient(base_url=internal_service_settings.base_url)
