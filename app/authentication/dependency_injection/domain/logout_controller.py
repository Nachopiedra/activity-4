from app.authentication.domain.controllers.logout_controller import LogoutController
from app.authentication.dependency_injection.persistences.token_persistences import (
    token_persistence,
)

logout_controller = LogoutController(token_persistence=token_persistence)
