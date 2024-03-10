from typing import Union
from fastapi import FastAPI
from ..models.DataController import controller

app = FastAPI()

@app.post("/toggle-favorite/{customer_id}/{product_id}", tags =["Product"])
def toggle_favorite(customer_id : int, product_id: int ):
    return controller.toggle_favorite(customer_id ,product_id )

@app.get("/favorite-list/{customer_id}", tags =["Product"])
def get_list_favorite(customer_id : int):
    return controller.view_favorite(customer_id)