from pydantic import BaseModel

class Item(BaseModel):
    name: str
    count: int

item = Item(name="apple", count="3")  # auto-casts str to int!
