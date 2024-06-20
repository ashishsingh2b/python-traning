from pydantic import BaseModel


class Todocreate(BaseModel):
    text : str

class Todoupdate(BaseModel):
    id:int
    text : str

class Tododelete(BaseModel):
    id:int
    