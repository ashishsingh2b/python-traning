from fastapi import FastAPI,Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import time

# Create an instance of FastAPI
app = FastAPI()

# Define a GET endpoint

class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self,request:Request,call_next):
        start_time =time.time()

        print(f"Request URL: {request.url}")
        response = await call_next(request)

        process_time = time.time() - start_time
        response.headers['X-Process-Time'] = str(process_time)
        return response
    
app.add_middleware(CustomMiddleware)


@app.get("/")
async def read_root():
    return {"message":"Hello Bro"}