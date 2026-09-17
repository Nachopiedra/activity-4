from app.authentication.domain.controllers.introspect_controller import (
    IntrospectController,
)
from app.authentication.dependency_injection.persistences.token_persistences import (
    token_persistence,
)
from app.authentication.dependency_injection.persistences.user_bo_persistences import (
    user_persistence,
)

introspect_controller = IntrospectController(
    token_persistence=token_persistence,
    user_persistence=user_persistence,
)
