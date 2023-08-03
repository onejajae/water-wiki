from pydantic import BaseModel


class Ping(BaseModel):
  content: str


class Pong(BaseModel):
  content: str


class EchoRequest(BaseModel):
  message: str


class EchoResponse(BaseModel):
  message: str