from fastapi import APIRouter

from .schema import EchoRequest, EchoResponse
from .services import _ping, _echo

router = APIRouter()

@router.get("/")
async def ping():
  pong = _ping()
  return {"ping": pong}


@router.post("/echo", response_model=EchoResponse)
async def echo(echo_message: EchoRequest):
  return _echo(echo_message)
