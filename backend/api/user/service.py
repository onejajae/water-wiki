from sqlalchemy.orm import Session

import jwt
from bcrypt import hashpw, gensalt, checkpw

from datetime import datetime, timedelta

from db.model import User
from .schema import UserCreate, Token

from config import Settings


def create_user(db: Session, user_in: UserCreate):
    hashed_password = hashpw(user_in.password.encode("utf-8"), gensalt())
    hashed_password = hashed_password.decode("utf-8")

    new_user = User(username=user_in.username, password=hashed_password, is_admin=False)
    db.add(new_user)
    db.commit()
    db.refresh()

    return db.query(User).filter(User.username == user_in.username).first()


def get_user(db: Session, username: str):
    user = db.query(User).filter(User.username == username).first()
    return user


def get_access_token(db: Session, username: str, settings: Settings) -> Token:
    user = db.query(User).filter(User.username == username).first()

    return Token(
        access_token=create_token(user, settings),
        username=user.username,
        admin=user.is_admin,
    )


def is_existing_user(db: Session, username) -> bool:
    user = db.query(User).filter(User.username == username).first()
    if user:
        return True
    else:
        return False


def authenticate_user(db: Session, username: str, password: str) -> bool:
    user = db.query(User).filter(User.username == username).first()
    return verify_password(password, user.password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))


def create_token(user: User, settings: Settings):
    payload = {
        "user_id": user.id,
        "username": user.username,
        "exp": datetime.utcnow() + timedelta(minutes=settings.jwt_exp_minute),
    }

    return jwt.encode(
        payload, key=settings.jwt_secret, algorithm=settings.jwt_hash_algorithm
    )


def verify_token(token: str, settings: Settings):
    decoded_token = jwt.decode(
        token, key=settings.jwt_secret, algorithms=settings.jwt_hash_algorithm
    )
    return decoded_token
