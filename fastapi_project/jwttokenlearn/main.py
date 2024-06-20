from typing import Annotated,Union
from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.security import OAuth2AuthorizationCodeBearer,OAuth2PasswordRequestForm,OAuth2PasswordBearer
from jose import jwt



app =FastAPI()

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

@app.post("/")
async def login(form_data:Annotated[OAuth2PasswordRequestForm,Depends()]):
    #return {"access_token":"token yahan per banan hai","token_type":"bearer"}
    if form_data.username != "Ashish":
        raise HTTPException (status_code=400,detail="Incorrect Username")
    
    if form_data.password != "Singh":
        raise HTTPException (status_code=400,detail="Incorrect Password")
    
    token = jwt.encode({"username":form_data.username},
                       "    abc",algorithm='HS256')
    return {"access_token":token}

@app.get("/user/me/")
async def user_api(token: Annotated[str,Depends(oauth2_scheme)]):
    return {"token": "yaha per token ko get karna hai"}



