from fastapi import FastAPI


app = FastAPI()

@app.get("/gettest")
async def greet():
    return {"message":"Good Morning Ashish"}


@app.get("/post")
async def post_item(item:item):
    return {"item_id":item_id,}