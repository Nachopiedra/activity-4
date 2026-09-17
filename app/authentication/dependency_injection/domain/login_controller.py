from app.authentication.dependency_injection.persistences.token_persistences import (
    token_persistence,
)
from app.authentication.dependency_injection.persistences.user_bo_persistences import (
    user_persistence,
)
from app.authentication.domain.controllers.login_controller import LoginController

login_controller = LoginController(
    user_persistence=user_persistence,
    token_persistence=token_persistence,
)
