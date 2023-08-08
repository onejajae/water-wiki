from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.router import router as api_router
from config import Settings, get_settings


def make_app(settings: Settings) -> FastAPI:
    if settings.app_mode == "prod":
        return FastAPI(title="Water Wiki", docs_url=None, redoc_url=None)
    else:
        return FastAPI(title="Water Wiki")


settings = get_settings()
app = make_app(settings)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allow_cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")
