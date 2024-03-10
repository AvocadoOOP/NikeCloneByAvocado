from typing import Union
from pydantic import BaseModel
from .models.DataController import controller

from fastapi import APIRouter, Body
router = APIRouter()

class ProductSelect(BaseModel):
    customer_id: int
    product_id: int
    color_id: int
    size : str
    amout : int

@router.post("/product-add-cart/", tags =["Product"])
async def add_to_cart(data : ProductSelect):
    return controller.add_to_cart(data.customer_id, data.product_id, data.color_id, data.size, data.amout)

@router.delete("/product-delete-cart/{customer_id}/{product_id}/{color_id}/{size}", tags =["Product"])
def delete_from_cart(customer_id : int ,product_id : int, color_id : int, size : str):
    return controller.delete_from_cart(customer_id, product_id, color_id, size)

@router.get("/cart/{customer_id}", tags =["Product"])
def get_shopping_cart(customer_id : int):
    return controller.shopping_cart(customer_id)
