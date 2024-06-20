from typing import Optional
async def common_operaotrs(q:Optional[str]="Shyam", skip:int=0,limit:int=100):
    return {"q":q,"skip":skip,"limit":limit}