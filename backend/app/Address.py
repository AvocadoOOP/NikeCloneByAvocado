from typing import Union
from pydantic import BaseModel
from .models.DataController import controller

from fastapi import APIRouter, Body
router = APIRouter()

class AddressIn(BaseModel):
    customer_id : int
    recipient_name  : str
    house_number : str
    soi : str
    road : str
    province : str
    postal_code : str
    phone : str

@router.post("/address-add/", tags =["Profile"])
def add_address(data : AddressIn):
    return controller.add_address(data.customer_id, data.recipient_name, data.house_number, data.soi, data.road, data.province, data.postal_code, data.phone)
@router.get("/address-list/{customer_id}/", tags =["Profile"])
def get_list_address(customer_id : int):
    return controller.view_address(customer_id)

@router.delete("/address-delete/{customer_id}/{address_id}/", tags =["Profile"])
def delete_address(customer_id : int ,address_id : int):
    return controller.delete_address(customer_id, address_id)

@router.get("/address-choose/{customer_id}/{address_id}/", tags =["Buy"])
def choose_address(customer_id : int, address_id : int):
    return controller.choose_address(customer_id, address_id)