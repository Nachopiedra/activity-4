from dataclasses import dataclass


@dataclass
class UserBO:
    """Minimal representation of an authenticated user, as seen by the files module."""

    username: str
