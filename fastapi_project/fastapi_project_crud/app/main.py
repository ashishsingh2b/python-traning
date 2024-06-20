from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from typing import List
from fastapi.security import OAuth2PasswordRequestForm
from app.database import database,engine
from app.models.models import Base, User, Product
from app.schemas.schemas import UserCreate, User as UserSchema, ProductCreate, Product as ProductSchema
from app.crud.crud import create_user, get_user_by_username, get_products, create_product, get_product, update_product, delete_product,get_password_hash
from app.auth.auth import authenticate_user, create_access_token, get_current_user, get_db
from app.schemas.schemas import Token

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=15)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# @app.post("/users/", response_model=UserSchema)
# async def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = get_user_by_username(db, username=user.username)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Username already registered")
#     return create_user(db=db, user=user)

# Endpoint to create a new user
# @app.post("/users/", response_model=UserSchema)
# async def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = get_user_by_username(db, username=user.username)
#     if db_user:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    
#     created_user = create_user(db=db, user=user)
#     return created_user

from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError

@app.post("/users/", response_model=UserSchema)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = get_user_by_username(db, username=user.username)
        if db_user:
            raise HTTPException(status_code=400, detail="Username already registered")
        
        hashed_password = get_password_hash(user.password)
        db_user = User(username=user.username, hashed_password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        return db_user
    except SQLAlchemyError as e:
        db.rollback()  # Rollback transaction on database error
        raise HTTPException(status_code=500, detail="Database error")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/users/me/", response_model=UserSchema)
async def read_users_me(current_user: UserSchema = Depends(get_current_user)):
    return current_user

@app.post("/products/", response_model=ProductSchema)
async def create_product(product: ProductCreate, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    return create_product(db=db, product=product)

@app.get("/products/", response_model=List[ProductSchema])
async def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    products = get_products(db, skip=skip, limit=limit)
    return products

@app.put("/products/{product_id}", response_model=ProductSchema)
async def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    return update_product(db=db, product_id=product_id, product=product)

@app.delete("/products/{product_id}", response_model=ProductSchema)
async def delete_product(product_id: int, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    return delete_product(db=db, product_id=product_id)
