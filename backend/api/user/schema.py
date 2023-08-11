from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    username: str
    admin: bool


class UserBase(BaseModel):
    username: str
    is_admin: bool
