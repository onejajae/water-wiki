from .schema import EchoRequest

def _ping():
  return "Pong"

def _echo(echo_message: EchoRequest):
  return {"message": echo_message.message+echo_message.message}
