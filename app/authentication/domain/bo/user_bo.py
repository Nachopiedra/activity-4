from dataclasses import dataclass


@dataclass
class UserBO:
    """Domain business object for a user.

    ``password`` is stored already hashed; the domain never keeps plain text.
    """

    username: str
    password: str
    mail: str
    age_of_birth: int
