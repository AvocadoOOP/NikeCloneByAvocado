from typing import Union
from ..models.DataController import controller
from fastapi import APIRouter, Body
router = APIRouter()

@router.post("/order-create/{customer_id}/{address_id}/", tags =["Buy"])
def create_order (customer_id : int, address_id : int ):
    return controller.create_order(customer_id, address_id)

@router.get("/order/{customer_id}/", tags =["Buy"])
def list_order(customer_id : int):
    return controller.view_order(customer_id)

@router.get("/order-check/", tags =["Admin"])
def check_order():
    return controller.check_order

@router.get("/order-update/{order_id}/", tags =["Admin"])
def update_order( order_id : int, admin_id : int, status: str):
    return controller.update_order(order_id, admin_id, status)