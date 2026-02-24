from typing import List
from fastapi import FastAPI
from pydantic import BaseModel,Field


class Item(BaseModel):
    name: str
    quantity: int =  Field(gt=0)

class Order(BaseModel):
    id : int
    items : List[Item]
    total_price : float = Field(ge=0)


app = FastAPI()

@app.post("/orders/")
async def post_order(order : Order):
    return {"order": order}