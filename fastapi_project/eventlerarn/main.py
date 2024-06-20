from fastapi import FastAPI

app = FastAPI()

#event handler for startup
@app.on_event("startup")
async def start_event():
    print("app is starting now!!!!!!!!!!!")


@app.on_event("shutdown")
async def shutdown_event():
    print("Closing the application please wait  !!!!!!!!!!!")


@app.get("/")
async def greeting():
    return {"message":"Hello Ashish"}