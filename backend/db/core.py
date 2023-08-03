from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

# Database Configurations


SQLALCHEMY_DATABASE_URL = 'sqlite:///test.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
                       "check_same_thread": False})
db_session = sessionmaker(bind=engine)


Base = declarative_base()

def get_db():
  db = db_session()
  try:
    yield db
  finally:
    db.close()

