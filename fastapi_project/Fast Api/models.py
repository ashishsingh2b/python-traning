from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name : str
    des : str
    price : Optional[int] = None