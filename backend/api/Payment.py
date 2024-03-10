from typing import Union
from ..models.DataController import controller

from fastapi import APIRouter, Body
router = APIRouter()

@router.get("/pay-money/{customer_id}/{number}/{order_id}/", tags =["Buy"])
def pay_money(customer_id : int, number : str, order_id : int):
    return controller.pay_money(customer_id, number, order_id)

@router.get("/product-buy/{customer_id}/", tags =["Buy"])
def buy_product(customer_id : int):
    return controller.buy_product(customer_id)
