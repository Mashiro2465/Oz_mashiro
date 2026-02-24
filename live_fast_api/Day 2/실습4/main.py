from fastapi import FastAPI
from pydantic import BaseModel, computed_field, field_validator

class Products(BaseModel):
    name : str
    price : float
    discount : float = 0

    @computed_field
    @property
    def final_price(self) -> float:
        discount_rate = self.discount/100
        return round(self.price * (1 - discount_rate),1)

    @field_validator('discount')
    @classmethod
    def discount_validator(cls, v : float):
        if v < 0:
            raise ValueError("Discount must be positive")
        if v > 100:
            raise ValueError("Discount must be less than 100")
        return v


app = FastAPI()

@app.post("/products/")
async def create_products(products: Products):
    return products
