from typing import Union
from pydantic import BaseModel
from .models.DataController import controller

from fastapi import APIRouter, Body
router = APIRouter()

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

@router.post("/register/", tags =["Register"])
def register(data : RegisterIn):
    return controller.register(data.username, data.email, data.password)

@router.post("/login/", tags =["Login"])
def login(data : LoginIn):
    return controller.login(data.email, data.password)

@router.get("/profile-view/", tags =["Profile"])
def view_profile(customer_id : int):
    return controller.view_profile(customer_id)

@router.get("/account-detail/", tags =["Profile"])
def detail_account(customer_id : int):
    return controller.view_account_detail(customer_id)

@router.put("/phone-add/", tags =["Profile"])
def update_phone(data : PhoneIn):
    return controller.update_phone(data.customer_id, data.phone)
