#******************What you have to do start with this *************

#install this first
#1.pip install fastapi
#2.pip install requests
#3.pip install unicorn
#4.pip install httpie

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return "Jay Shree Ram","Jay Bajrang Baan"


@app.get('/items/{item_id}')
def items(item_id:int):
    return {'item_id':item_id}

@app.get('/{product}/items/{item_id}')
def item2(item_id:int,product:str):
    return{'id':item_id, 'product_name':product}
