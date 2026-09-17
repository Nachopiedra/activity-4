from typing import Optional

from fastapi import APIRouter, Body, File, Header, HTTPException, UploadFile
from pydantic import BaseModel

from app.files.dependency_injection.domain.create_file_controller import (
    create_file_controller,
)
from app.files.dependency_injection.domain.delete_file_controller import (
    delete_file_controller,
)
from app.files.dependency_injection.domain.get_file_controller import (
    get_file_controller,
)
from app.files.dependency_injection.domain.list_files_controller import (
    list_files_controller,
)
from app.files.dependency_injection.domain.merge_controller import merge_controller
from app.files.dependency_injection.domain.upload_content_controller import (
    upload_content_controller,
)
from app.files.domain.persistences.exceptions import (
    FileContentNotFoundException,
    FileNotFoundException,
    UnauthorizedException,
)

router = APIRouter()


class FileOutput(BaseModel):
    id: int
    owner_username: str
    title: str
    author: str
    has_content: bool
    object_name: Optional[str] = None


class CreateFileInput(BaseModel):
    title: str
    author: str


class MergeInput(BaseModel):
    file_ids: list[int]


@router.get("")
async def list_files(auth: str = Header()) -> list[FileOutput]:
    try:
        files = await list_files_controller.list_files(auth)
    except UnauthorizedException:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return [FileOutput(**file.__dict__) for file in files]


@router.post("")
async def create_file(auth: str = Header(), input: CreateFileInput = Body()) -> int:
    try:
        file = await create_file_controller.create_file(
            token=auth, title=input.title, author=input.author
        )
    except UnauthorizedException:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return file.id


@router.post("/merge")
async def merge_files(auth: str = Header(), input: MergeInput = Body()) -> int:
    try:
        merged = await merge_controller.merge(token=auth, file_ids=input.file_ids)
    except UnauthorizedException:
        raise HTTPException(status_code=401, detail="Unauthorized")
    except FileNotFoundException:
        raise HTTPException(status_code=404, detail="File not found")
    except FileContentNotFoundException:
        raise HTTPException(status_code=404, detail="File content not found")
    return merged.id


@router.get("/{id}")
async def get_file(id: int, auth: str = Header()) -> FileOutput:
    try:
        file = await get_file_controller.get_file(token=auth, file_id=id)
    except UnauthorizedException:
        raise HTTPException(status_code=401, detail="Unauthorized")
    except FileNotFoundException:
        raise HTTPException(status_code=404, detail="File not found")
    return FileOutput(**file.__dict__)


@router.post("/{id}")
async def upload_content(
    id: int, auth: str = Header(), file_content: UploadFile = File()
) -> dict[str, str]:
    content = await file_content.read()
    try:
        await upload_content_controller.upload_content(token=auth, file_id=id, content=content)
    except UnauthorizedException:
        raise HTTPException(status_code=401, detail="Unauthorized")
    except FileNotFoundException:
        raise HTTPException(status_code=404, detail="File not found")
    return {"status": "ok"}


@router.delete("/{id}")
async def delete_file(id: int, auth: str = Header()) -> dict[str, str]:
    try:
        await delete_file_controller.delete_file(token=auth, file_id=id)
    except UnauthorizedException:
        raise HTTPException(status_code=401, detail="Unauthorized")
    except FileNotFoundException:
        raise HTTPException(status_code=404, detail="File not found")
    return {"status": "ok"}
