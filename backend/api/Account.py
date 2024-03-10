from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from ..models.DataController import controller

app = FastAPI()

class RegisterIn(BaseModel):
    username: str
    email: str
    password: str

class LoginIn(BaseModel):
    email: str
    password: str

class PhoneIn(BaseModel):
    customer_id : int
    phone : str

@app.post("/register/", tags =["Register"])
def register(data : RegisterIn):
    return controller.register(data.username, data.email, data.password)

@app.post("/Login/", tags =["Login"])
def login(data : LoginIn):
    return controller.login(data.email, data.password)

@app.get("/profile-view/{order_id}/", tags =["Profile"])
def view_profile(customer_id : int):
    return controller.view_profile(customer_id)

@app.get("/account-detail/{order_id}/", tags =["Profile"])
def detail_account(customer_id : int):
    return controller.view_account_detail(customer_id)

@app.put("/phone-add/", tags =["Profile"])
def update_phone(data : PhoneIn):
    return controller.update_phone(data.customer_id, data.phone)
