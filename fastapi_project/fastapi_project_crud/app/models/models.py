from sqlalchemy import Column,Integer,String,Float,DateTime,func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__="users"
    id= Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,index=True)
    hashed_password = Column(String)

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)  # Use Float instead of float
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    updated_at = Column(DateTime(timezone=True),onupdate=func.now())