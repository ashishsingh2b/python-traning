from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database

DATABASE_URL = "postgresql://postgres:password123#@localhost/fastapi_crud"

database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

from sqlalchemy.orm import Session
from app.database import SessionLocal

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

