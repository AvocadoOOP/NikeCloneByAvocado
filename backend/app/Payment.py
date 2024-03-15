from typing import Union
from .models.DataController import controller

from fastapi import APIRouter, Body
router = APIRouter()

@router.get("/pay-money/{customer_id}/{address_id}/{number}", tags =["Buy"])
def pay_money(customer_id : str, address_id : str, number : str):
    return controller.pay_money(int(customer_id), int(address_id), number)