from pydantic import BaseModel


class UserBase(BaseModel):
  username: str


class Token(BaseModel):
  username: str