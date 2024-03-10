from typing import Union

from pydantic import BaseModel
from ..models.DataController import controller

from fastapi import APIRouter, Body
router = APIRouter()

class CreditCardIn(BaseModel):
    customer_id : int
    type_card : str
    card_name : str
    number : str
    pin_number : int

@router.post("/credit-add/", tags =["Profile"])
def add_credit_card(data :CreditCardIn):
    return controller.add_credit_card(data.customer_id, data.type_card, data.card_name, data.number, data.pin_number)

@router.get("/credit-list/{customer_id}/", tags =["Profile"])
def list_credit_card(customer_id : int):
    return controller.view_credit_card(customer_id)

@router.delete("/credit-delete/{customer_id}/{number}/", tags =["Profile"])
def delete_credit_card(customer_id : int , number : str):
    return controller.delete_credit_card(customer_id, number)

@router.get("/credit-choose/{customer_id}/{credit_id}/", tags =["Buy"])
def  choose_credit(customer_id : int, credit_id : int):
    return controller.choose_credit(customer_id, credit_id)