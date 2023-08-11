from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

from config import get_settings

# Database Configurations

settings = get_settings()

SQLALCHEMY_DATABASE_URL = settings.db_host
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
db_session = sessionmaker(bind=engine)


Base = declarative_base()


def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()
