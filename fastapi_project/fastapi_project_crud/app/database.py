# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from databases import Database


# #DATABASE_URL = 'postgresql://postgres:password123@localhost:5432/fastapi_crud'
# # Example database URL format for PostgreSQL
# DATABASE_URL = "postgresql://postgres:password123#@localhost:5432/fastapi_crud"



# database  = Database(DATABASE_URL)
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit =False,autoflush=False,bind=engine)

# Base = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database

# Corrected DATABASE_URL
DATABASE_URL = "postgresql://postgres:password123%23@localhost:5432/fastapi_crud"

# SQLAlchemy engine and session setup
database  = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Example of how to use the sessionmaker
# Example: session = SessionLocal()
