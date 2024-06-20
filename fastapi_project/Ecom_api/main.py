from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

register_tortoise(
    app,
    db_url='postgres://username:password@localhost:5432/databasename',
    modules={'models': ['Ecom_api.models']},  # Replace with the actual path to your models
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

























# from fastapi import FastAPI
# from tortoise import models
# from tortoise.contrib.fastapi import register_tortoise
# from models import *

# app =FastAPI()

# @app.get("/")
# def index():
#     return {"Greeting":"Hello Word"}

# register_tortoise (
#     app,
#     db_url="postgresql://postgres:password123%23@localhost:5432/Ecom_proj",
#     models = {"models":["models"]},
#     generate_schemas=True,
#     add_exception_handlers=True
# )