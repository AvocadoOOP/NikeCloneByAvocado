from typing import Union
from ..models.DataController import controller

from fastapi import APIRouter, Body
router = APIRouter()

@router.post("/toggle-favorite/{customer_id}/{product_id}", tags =["Product"])
def toggle_favorite(customer_id : int, product_id: int ):
    return controller.toggle_favorite(customer_id ,product_id )

@router.get("/favorite-list/{customer_id}", tags =["Product"])
def get_list_favorite(customer_id : int):
    return controller.view_favorite(customer_id)