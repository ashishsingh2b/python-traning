
from jose import jwt

ALGORITHM = "HS256"
SECRET = "I AM SECRET KEY"
 
def create_access_token(subject: str):
    token = jwt.encode({"data": subject}, SECRET, algorithm=ALGORITHM)
    return {"access_token": token}

def decode_token(token: str):
    data = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
    return data
