# from fastapi import FastAPI

# api=FastAPI()

# @api.post('/items')
# async def read_item():
#     return 'post request'


from fastapi import FastAPI,Body
from models import Item

api=FastAPI()

@api.post('/items')
async def read_item(item:Item):
    return item.name

@api.put("/items/{item_id}")
async def updtae_item(item_id:int,item:Item):
    return {"item_id":item_id, **item.dict()}

@api.post("/items/item")
async def read_item1(item:str=Body(embed=True)):
    return item