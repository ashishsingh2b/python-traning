from fastapi import FastAPI

api = FastAPI()

# @api.get('/')
# def hello():
#     return "Jay Jay Shree Ramjii"

@api.get('/items')
def Haahaa(q:int = 0, skip:int =500):
    return {"q":q, "skip":skip}