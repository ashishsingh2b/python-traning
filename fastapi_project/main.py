from typing import Annotated,Union
from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.security import OAuth2AuthorizationCodeBearer,OAuth2PasswordRequestForm
from jose import jwt


app =FastAPI()


@app.post("/")
async def login(form_data:Annotated[OAuth2PasswordRequestForm,Depends()]):
    #return {"access_token":"token yahan per banan hai","token_type":"bearer"}
    if form_data.username != "Ashish":
        raise HTTPException (status_code=400,detail="Incorrect Username")
    
    if form_data.password != "Singh":
        raise HTTPException (status_code=400,detail="Incorrect Password")
    
    token = jwt.encode({"username":form_data.username},
                       "    abc",algorithm='HS256')
    return {"token":token}    


