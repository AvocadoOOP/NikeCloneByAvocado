from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from ..models.DataController import controller

app = FastAPI()

class ProductSelect(BaseModel):
    customer_id: int
    product_id: int
    color_id: int
    size : str
    amout : int

@app.post("/product-add-cart/", tags =["Product"])
async def add_to_cart(data : ProductSelect):
    return controller.add_to_cart(data.customer_id, data.product_id, data.color_id, data.size, data.amout)

@app.delete("/product-delete-cart/{customer_id}/{product_id}/{color_id}/{size}", tags =["Product"])
def delete_from_cart(customer_id : int ,product_id : int, color_id : int, size : str):
    return controller.delete_from_cart(customer_id, product_id, color_id, size)

@app.get("/cart/{customer_id}", tags =["Product"])
def get_shopping_cart(customer_id : int):
    return controller.shopping_cart(customer_id)
