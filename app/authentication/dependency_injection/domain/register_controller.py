from app.authentication.domain.controllers.register_controller import RegisterController
from app.authentication.dependency_injection.persistences.user_bo_persistences import (
    user_persistence,
)

register_controller = RegisterController(user_persistence=user_persistence)

