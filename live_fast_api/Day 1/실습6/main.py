from itertools import product

from pydantic import BaseModel, Field
from fastapi import FastAPI

app = FastAPI()


class Product(BaseModel):
    name : str
    price : float = Field(gt=0, description="Price must be greater than 0")
    description : str = "No description"


@app.get("/products/")
async def get_products(product :Product):
    return {"product": product}
