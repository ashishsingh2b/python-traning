from fastapi import FastAPI

app = FastAPI()

@get("/")
async def root():
    return {"message":"Hello"}
    
 