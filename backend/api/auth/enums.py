from enum import Enum


class Token(str, Enum):
    def __str__(self) -> str:
        return str.__str__(self)