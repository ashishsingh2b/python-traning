from fastapi import FastAPI,Depends
from dependency import common_operaotrs
from typing import Annotated
app=FastAPI()

#***************************Method 1 *****************************

@app.get('/items')
async def read_items(commons:dict = Depends(common_operaotrs)):
    return commons


@app.get('/user')
async def read_items(commons:dict = Depends(common_operaotrs)):
    return commons

#***********************Method With Annotated**********************


@app.get('/items')
async def read_items(commons:Annotated[dict,Depends(common_operaotrs)]):
    return commons


@app.get('/user')
async def read_items(commons:Annotated[dict,Depends(common_operaotrs)]):
    return commons
#***********************Method With Annotated in a variable**********************

Commondepends = Annotated[dict,Depends(common_operaotrs)]

@app.get('/user')
async def read_readline(commons:Commondepends):
    return commons


@app.get('/items')
async def read_readline(commons:Commondepends):
    return commons