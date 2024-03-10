from fastapi import FastAPI
from . import  Account, Address , CreditCard , Favorite , Order , Payment , Product , ShoppingCart
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:5500",
    "localhost:5500",
    "http://127.0.0.1:5500",
    "127.0.0.1:5500"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(Account.router)
app.include_router(Address.router)
app.include_router(CreditCard.router)
app.include_router(Favorite.router)
app.include_router(Order.router)
app.include_router(Payment.router)
app.include_router(Product.router)
app.include_router(ShoppingCart.router)


@app.get("/")
async def read_root():
    return {"message": "Yo!!! it's Pat Pookkie Praewa Mew right here!!!!"}