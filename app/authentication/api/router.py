from fastapi import APIRouter, Body, Header, HTTPException
from pydantic import BaseModel

from app.authentication.dependency_injection.domain.introspect_controller import (
    introspect_controller,
)
from app.authentication.dependency_injection.domain.login_controller import (
    login_controller,
)
from app.authentication.dependency_injection.domain.logout_controller import (
    logout_controller,
)
from app.authentication.dependency_injection.domain.register_controller import (
    register_controller,
)
from app.authentication.domain.persistences.exceptions import (
    TokenNotFound,
    UsernameAlreadyTakenException,
    UserNotFoundException,
    WrongPasswordException,
)

router = APIRouter()


class RegisterInput(BaseModel):
    username: str
    password: str
    mail: str
    age_of_birth: int


class RegisterOutput(BaseModel):
    username: str
    mail: str
    age_of_birth: int


@router.post("/register")
async def register_post(input: RegisterInput = Body()) -> RegisterOutput:
    try:
        user = register_controller.register(
            username=input.username,
            password=input.password,
            mail=input.mail,
            age_of_birth=input.age_of_birth,
        )
    except UsernameAlreadyTakenException:
        raise HTTPException(status_code=409, detail="This username is already taken")
    return RegisterOutput(
        username=user.username,
        mail=user.mail,
        age_of_birth=user.age_of_birth,
    )


class LoginInput(BaseModel):
    username: str
    password: str


@router.post("/login")
async def login_post(input: LoginInput = Body()) -> dict[str, str]:
    try:
        token = login_controller.login(username=input.username, password=input.password)
    except UserNotFoundException:
        raise HTTPException(status_code=404, detail="User not found")
    except WrongPasswordException:
        raise HTTPException(status_code=403, detail="Password is not correct")
    return {"auth": token}


@router.post("/logout")
async def logout_post(auth: str = Header()) -> dict[str, str]:
    try:
        logout_controller.logout(auth)
    except TokenNotFound:
        raise HTTPException(status_code=403, detail="Forbidden")
    return {"status": "ok"}


class IntrospectOutput(BaseModel):
    username: str
    mail: str
    age_of_birth: int


@router.get("/introspect")
async def introspect_get(auth: str = Header()) -> IntrospectOutput:
    try:
        user = introspect_controller.introspect(auth)
    except TokenNotFound:
        raise HTTPException(status_code=403, detail="Forbidden")
    return IntrospectOutput(
        username=user.username,
        mail=user.mail,
        age_of_birth=user.age_of_birth,
    )
