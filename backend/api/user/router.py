from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from db.core import get_db

from .service import is_existing_user, create_user, get_user
from .schema import UserCreate, Token

router = APIRouter()


@router.post("/register")
async def register(user_in: UserCreate, db: Session = Depends(get_db)):
  if not is_existing_user(db=db, username=user_in.username):
    raise HTTPException(status_code=status.HTTP_409_CONFLICT)
  
  create_user(db=db, user_in=user_in)


@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), 
                db: Session = Depends(get_db)):
  
  if not is_existing_user(db=db, username=form_data.username):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
  
  user_token = get_user(db=db, username=form_data.username, password=form_data.password)
  if user_token is None:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
  
  return user_token