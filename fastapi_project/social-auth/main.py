from fastapi import FastAPI,Depends,Request
from authlib .integrations.starlette_client import OAuth
from fastapi.responses import JSONResponse
from starlette.middleware.sessions import SessionMiddleware



app = FastAPI()

oauth = OAuth()

SECRET_KEY = "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"

app.add_middleware(SessionMiddleware,secret_key=SECRET_KEY)



oauth.register(
    name="google",
    client_id ="336940855313-6no1ro9pvrur1r1j6kk3rluroob9astf.apps.googleusercontent.com",
    client_secret = "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",
    authorize_url = "https://accounts.google.com/o/oauth2/auth",
    client_kwargs = {"scope":"openid profile email"},

)

@app.get("/login")
async def login(request:Request):
    redirect_url = request.url_for("auth")
    authorization_url=await oauth.google.authorize_redirect(request, redirect_url)
    return authorization_url

@app.get("/auth")
async def auth(request):
    token =await oauth.google.authorize_access_token(request)
    user = await oauth.google.parse_id_token(request,token)
    return JSONResponse(content={"user":user})


    

