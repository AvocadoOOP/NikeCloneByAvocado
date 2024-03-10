from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from ..models.DataController import controller

app = FastAPI()

class AddressIn(BaseModel):
    customer_id : int
    house_number : str
    soi : str
    road : str
    province : str
    postal_code : str

@app.post("/address-add/", tags =["Profile"])
def add_address(data : AddressIn):
    return controller.add_address(data.customer_id, data.house_number, data.soi, data.road, data.province, data.postal_code)

@app.get("/address-list/{customer_id}/", tags =["Profile"])
def get_list_address(customer_id : int):
    return controller.view_address(customer_id)

@app.delete("/address-delete/{customer_id}/{address_id}/", tags =["Profile"])
def delete_address(customer_id : int ,address_id : int):
    return controller.delete_address(customer_id, address_id)

@app.get("/address-choose/{customer_id}/{address_id}/", tags =["Buy"])
def choose_address(customer_id : int, address_id : int):
    return controller.choose_address(customer_id, address_id)