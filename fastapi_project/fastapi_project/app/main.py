from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.database import engine, database
from app.models.models import Base, User, Product
from app.schemas.schemas import UserCreate, User, ProductCreate, Product
from app.crud.crud import create_user, get_user_by_username, get_products, create_product, get_product, update_product, delete_product
from app.auth.auth import authenticate_user, create_access_token, get_current_user, get_db

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
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=User)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db=db, user=user)

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.post("/products/", response_model=Product)
async def create_product(product: ProductCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_product(db=db, product=product)

@app.get("/products/", response_model=List[Product])
async def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    products = get_products(db, skip=skip, limit=limit)
    return products

@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return update_product(db=db, product_id=product_id, product=product)

@app.delete("/products/{product_id}", response_model=Product)
async def delete_product(product_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    delete_product(db=db, product_id=product_id)
    return {"message": "Product deleted successfully"}

