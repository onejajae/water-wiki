from datetime import datetime

from .schema import HealthCheck
from config import Settings


def get(settings: Settings) -> HealthCheck:
    current_time: datetime = datetime.now()
    return HealthCheck(
        status="OK", app_mode=settings.app_mode, current_time=current_time
    )
