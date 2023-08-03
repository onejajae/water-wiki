from sqlalchemy.orm import Session
from db.models import User

from .schema import UserCreate, Token

from bcrypt import hashpw, gensalt, checkpw
from datetime import datetime, timedelta
import jwt

def create_user(db: Session, user_in: UserCreate):
  hashed_password = hashpw(user_in.password.encode("utf-8"), gensalt())
  hashed_password = hashed_password.decode("utf-8")

  new_user = User(username=user_in.username, password=hashed_password, is_admin=False)
  db.add(new_user)
  db.commit()

def get_user(db: Session, username: str, password: str):
  user = db.query(User).filter(User.username == username).first()
  
  if not checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
    return None
  
  return Token(
    access_token=create_token(user),
    username=user.username,
    admin=True
  )

def is_existing_user(db: Session, username):
  user = db.query(User).filter(User.username == username).first()
  if user:
    return True
  else:
    return False
  
def create_token(user: User):
  payload = {
    'user_id': user.id,
    'username': user.username,
    'exp': (datetime.utcnow() + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
  }

  SECRET_KEY = "secret"
  return jwt.encode(payload, SECRET_KEY, algorithm='HS256')