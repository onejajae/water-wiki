from fastapi import APIRouter, Depends

from .schema import HealthCheck
from .services import get
from config import Settings, get_settings

router = APIRouter()


@router.get("/", response_model=HealthCheck)
async def get_health(settings: Settings = Depends(get_settings)):
    return get(settings=settings)
