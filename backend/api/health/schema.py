from datetime import datetime

from pydantic import BaseModel


class HealthCheck(BaseModel):
    status: str = "OK"
    app_mode: str
    current_time: datetime
