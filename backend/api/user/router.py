from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from sqlalchemy.orm import Session
from db.core import get_db

from .service import (
    is_existing_user,
    create_user,
    get_user,
    get_access_token,
    verify_token,
    authenticate_user,
)
from .schema import UserCreate, Token

from config import Settings, get_settings

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/login")


@router.post("/register")
async def register(
    user_in: UserCreate,
    db: Session = Depends(get_db),
    settings: Settings = Depends(get_settings),
):
    # temporarily disabled in production
    if settings.app_mode == "prod":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    if is_existing_user(db=db, username=user_in.username):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)

    return create_user(db=db, user_in=user_in)


@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
    settings: Settings = Depends(get_settings),
):
    if not is_existing_user(db=db, username=form_data.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    if not authenticate_user(
        db=db, username=form_data.username, password=form_data.password
    ):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    user_token = get_access_token(
        db=db,
        username=form_data.username,
        settings=settings,
    )

    return user_token


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
    settings: Settings = Depends(get_settings),
):
    try:
        payload = verify_token(token=token, settings=settings)
        username: str = payload.get("username")
        if username is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    user = get_user(db=db, username=username)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return user


@router.get("/me")
async def me(current_user=Depends(get_current_user)):
    return current_user
