from fastapi import FastAPI
from functions import create_access_token,decode_token

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/create-token/")
async def create_token_api(name: str):
    token = create_access_token(subject=name)
    return token

@app.get("/decode-token/")
async def decode_token_api(token: str):
    data = decode_token(token=token)
    return data
