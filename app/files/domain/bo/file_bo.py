from dataclasses import dataclass
from typing import Optional


@dataclass
class FileBO:
    """Domain business object for a file's metadata (never its content).

    ``object_name`` is the identifier under which the content is stored in the
    object storage; it is set once the content has been uploaded.
    """

    id: int
    owner_username: str
    title: str
    author: str
    has_content: bool = False
    object_name: Optional[str] = None
