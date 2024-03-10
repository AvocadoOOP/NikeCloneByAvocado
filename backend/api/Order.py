from typing import Union
from fastapi import FastAPI
from ..models.DataController import controller

app = FastAPI()

@app.post("/order-create/{customer_id}/{address_id}/", tags =["Buy"])
def create_order (customer_id : int, address_id : int ):
    return controller.create_order(customer_id, address_id)

@app.get("/order/{customer_id}/", tags =["Buy"])
def list_order(customer_id : int):
    return controller.view_order(customer_id)

@app.get("/order-check/", tags =["Admin"])
def check_order():
    return controller.check_order

@app.get("/order-update/{order_id}/", tags =["Admin"])
def update_order( order_id : int, admin_id : int, status: str):
    return controller.update_order(order_id, admin_id, status)