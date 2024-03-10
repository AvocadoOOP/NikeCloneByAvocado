from typing import Union
from fastapi import FastAPI
from ..models.DataController import controller

app = FastAPI()

@app.get("/pay-money/{customer_id}/{number}/{order_id}/", tags =["Buy"])
def pay_money(customer_id : int, number : str, order_id : int):
    return controller.pay_money(customer_id, number, order_id)

@app.get("/product-buy/{customer_id}/", tags =["Buy"])
def buy_product(customer_id : int):
    return controller.buy_product(customer_id)
