from typing import Union
from pydantic import BaseModel
from .models.DataController import controller

from fastapi import APIRouter, Body
router = APIRouter()

#Men1
controller.add_product("Nike Air Force 1'07", 5200, "Men",
    {
        "Black": [100, "S"],
        "Black": [100, "M"],
        "Black": [100, "L"],
        "Puce": [50, "S"],
        "Puce": [50, "M"],
        "Puce": [50, "L"],
        "Grey": [80, "S"],
        "Grey": [80, "M"],
        "Grey": [80, "L"],
    }
)
#Men2
controller.add_product("Air Fox", 4500, "Men",
    {
        "Black": [80, "S"],
        "Black": [80, "M"],
        "Black": [80, "L"],
        "Yellow": [50, "S"],
        "Yellow": [50, "M"],
        "Yellow": [50, "L"],
        "Grey": [50, "S"],
        "Grey": [50, "M"],
        "Grey": [50, "L"],
    }
)
#Men3
controller.add_product("Nike Air Jojo", 4200, "Men",
    {
        "Orange": [100, "S"],
        "Orange": [100, "M"],
        "Orange": [100, "L"],
        "Blue": [100, "S"],
        "Blue": [100, "M"],
        "Blue": [100, "L"],
        "White": [100, "S"],
        "White": [100, "M"],
        "White": [100, "L"],
    }
)
#Men4
controller.add_product("Air Popcorn 4", 5000, "Men",
    {
        "Black": [100, "S"],
        "Black": [100, "M"],
        "Black": [100, "L"],
        "Mint": [30, "S"],
        "Mint": [30, "M"],
        "Mint": [30, "L"],
        "Pink": [50, "S"],
        "Pink": [50, "M"],
        "Pink": [50, "L"],
    }
)
#Men5
controller.add_product("Air Popcorn 9 By Me", 6100, "Men",
    {
        "Brown": [100, "S"],
        "Brown": [100, "M"],
        "Brown": [100, "L"],
        "Red": [70, "S"],
        "Red": [70, "M"],
        "Red": [70, "L"],
        "Green": [100, "S"],
        "Green": [100, "M"],
        "Green": [100, "L"],
    }
)
#Men6
controller.add_product("Nike Taba", 3500, "Men",
    {
        "Aquamarine": [50, "S"],
        "Aquamarine": [50, "M"],
        "Aquamarine": [50, "L"],
        "Lime": [30, "S"],
        "Lime": [30, "M"],
        "Lime": [30, "L"],
        "Black": [50, "S"],
        "Black": [50, "M"],
        "Black": [50, "L"],
    }
)
#Men7
controller.add_product("Sum Vanom", 4500, "Men",
    {
        "Green": [50, "S"],
        "Green": [50, "M"],
        "Green": [50, "L"],
        "Blue": [30, "S"],
        "Blue": [30, "M"],
        "Blue": [30, "L"],
        "Black": [200, "S"],
        "Black": [200, "M"],
        "Black": [200, "L"],
    }
)
#Men8
controller.add_product("Nike Min Drift", 7000, "Men",
    {
        "White": [100, "S"],
        "White": [100, "M"],
        "White": [100, "L"],
        "Green": [50, "S"],
        "Green": [50, "M"],
        "Green": [50, "L"],
        "Red": [60, "S"],
        "Red": [60, "M"],
        "Red": [60, "L"],
    }
)
#Men9
controller.add_product("Air Max 80", 6500, "Men",
    {
        "Navy blue": [100, "S"],
        "Navy blue": [100, "M"],
        "Navy blue": [100, "L"],
        "Blue": [70, "S"],
        "Blue": [70, "M"],
        "Blue": [70, "L"],
        "Green": [80, "S"],
        "Green": [80, "M"],
        "Green": [80, "L"],
    }
)
#Men10
controller.add_product("Hard OOP 4", 3300, "Men",
    {
        "Lime": [50, "S"],
        "Lime": [50, "M"],
        "Lime": [50, "L"],
        "Grey": [50, "S"],
        "Grey": [50, "M"],
        "Grey": [50, "L"],
        "Black": [80, "S"],
        "Black": [80, "M"],
        "Black": [80, "L"],
    }
)
#Men11
controller.add_product("Air Max 27", 6400, "Men",
    {
        "Orange": [100, "S"],
        "Orange": [100, "M"],
        "Orange": [100, "L"],
        "Purple": [80, "S"],
        "Purple": [80, "M"],
        "Purple": [80, "L"],
        "Pink": [50, "S"],
        "Pink": [50, "M"],
        "Pink": [50, "L"],
    }
)
#Men12
controller.add_product("Air Max Hippo", 5600, "Men",
    {
        "Cyan": [50, "S"],
        "Cyan": [50, "M"],
        "Cyan": [50, "L"],
        "Black": [100, "S"],
        "Black": [100, "M"],
        "Black": [100, "L"],
        "Green": [60, "S"],
        "Green": [60, "M"],
        "Green": [60, "L"],
    }
)
#Men13
controller.add_product("Nike Air Luk", 7800, "Men",
    {
        "Blue": [50, "S"],
        "Blue": [50, "M"],
        "Blue": [50, "L"],
        "Black": [100, "S"],
        "Black": [100, "M"],
        "Black": [100, "L"],
        "White": [50, "S"],
        "White": [50, "M"],
        "White": [50, "L"],
    }
)
#Men14
controller.add_product("Y2K Men 01", 5700, "Men",
    {
        "Brown": [100, "S"],
        "Brown": [100, "M"],
        "Brown": [100, "L"],
        "Blue": [80, "S"],
        "Blue": [80, "M"],
        "Blue": [80, "L"],
        "Black": [100, "S"],
        "Black": [100, "M"],
        "Black": [100, "L"],
    }
)
#Men15
controller.add_product("Air Shell 70", 4000, "Men",
    {
        "Pink": [100, "S"],
        "Pink": [100, "M"],
        "Pink": [100, "L"],
        "Green": [50, "S"],
        "Green": [50, "M"],
        "Green": [50, "L"],
        "Orange": [60, "S"],
        "Orange": [60, "M"],
        "Orange": [60, "L"],
    }
)
#Women1
controller.add_product("Nike taba", 4400, "Women",
    {
        "Black": [100, "S"],
        "Black": [100, "M"],
        "Black": [100, "L"],
        "Mint": [50, "S"],
        "Mint": [50, "M"],
        "Mint": [50, "L"],
        "Puce": [50, "S"],
        "Puce": [50, "M"],
        "Puce": [50, "L"],
    }
)
#Women2
controller.add_product("Nike Air Force 1'09", 5000, "Women",
    {
        "Black": [100, "S"],
        "Black": [100, "M"],
        "Black": [100, "L"],
        "Brown": [80, "S"],
        "Brown": [80, "M"],
        "Brown": [80, "L"],
        "Pink": [80, "S"],
        "Pink": [80, "M"],
        "Pink": [80, "L"],
    }
)
#Women3
controller.add_product("Princess 19", 5500, "Women",
    {
        "Pink": [100, "S"],
        "Pink": [100, "M"],
        "Pink": [100, "L"],
        "Black": [100, "S"],
        "Black": [100, "M"],
        "Black": [100, "L"],
        "Grey": [50, "S"],
        "Grey": [50, "M"],
        "Grey": [50, "L"],
    }
)
#Women4
controller.add_product("Air Max 12", 4700, "Women",
    {
        "Grey": [70, "S"],
        "Grey": [70, "M"],
        "Grey": [70, "L"],
        "Black": [80, "S"],
        "Black": [80, "M"],
        "Black": [80, "L"],
        "Purple": [60, "S"],
        "Purple": [60, "M"],
        "Purple": [60, "L"],
    }
)
#Women5
controller.add_product("Nike Pegasus 39", 6000, "Women",
    {
        "Mint": [80, "S"],
        "Mint": [80, "M"],
        "Mint": [80, "L"],
        "Pink": [80, "S"],
        "Pink": [80, "M"],
        "Pink": [80, "L"],
        "Black": [80, "S"],
        "Black": [80, "M"],
        "Black": [80, "L"],
    }
)
#Women6
controller.add_product("Air Vampire Max ", 7700, "Women",
    {
        "Red": [100, "S"],
        "Red": [100, "M"],
        "Red": [100, "L"],
        "Green": [80, "S"],
        "Green": [80, "M"],
        "Green": [80, "L"],
        "Black": [80, "S"],
        "Black": [80, "M"],
        "Black": [80, "L"],
    }
)
#Women7
controller.add_product("Nike Fura Plus", 5600, "Women",
    {
        "Puce": [100, "S"],
        "Puce": [100, "M"],
        "Puce": [100, "L"],
        "Colorful": [70, "S"],
        "Colorful": [70, "M"],
        "Colorful": [70, "L"],
        "Orange": [50, "S"],
        "Orange": [50, "M"],
        "Orange": [50, "L"],
    }
)
#Women8
controller.add_product("Sum Vanom", 4200, "Women",
    {
        "Green": [50, "S"],
        "Green": [50, "M"],
        "Green": [50, "L"],
        "Blue": [40, "S"],
        "Blue": [40, "M"],
        "Blue": [40, "L"],
        "Black": [100, "S"],
        "Black": [100, "M"],
        "Black": [100, "L"],
    }
)  
#Women9
controller.add_product("Solo Max By Me", 3900, "Women",
    {
        "Pink": [70, "S"],
        "Pink": [70, "M"],
        "Pink": [70, "L"],
        "Cyan": [50, "S"],
        "Cyan": [50, "M"],
        "Cyan": [50, "L"],
        "Black": [80, "S"],
        "Black": [80, "M"],
        "Black": [80, "L"],
    }
)
#Women10
controller.add_product("Nike Revo Hip", 5200, "Women",
    {
        "Cyan": [60, "S"],
        "Cyan": [60, "M"],
        "Cyan": [60, "L"],
        "Pink": [70, "S"],
        "Pink": [70, "M"],
        "Pink": [70, "L"],
        "Black": [80, "S"],
        "Black": [80, "M"],
        "Black": [80, "L"],
    }
)
#Women11
controller.add_product("Nike Air Zion Mood", 4700, "Women",
    {
        "White": [100, "S"],
        "White": [100, "M"],
        "White": [100, "L"],
        "Neon": [60, "S"],
        "Neon": [60, "M"],
        "Neon": [60, "L"],
        "Blue": [80, "S"],
        "Blue": [80, "M"],
        "Blue": [80, "L"],
    }
)
#Women12
controller.add_product("Area 51", 5100, "Women",
    {
        "Purple": [80, "S"],
        "Purple": [80, "M"],
        "Purple": [80, "L"],
        "Black": [80, "S"],
        "Black": [80, "M"],
        "Black": [80, "L"],
        "Colorful": [70, "S"],
        "Colorful": [70, "M"],
        "Colorful": [70, "L"],
    }
)
#Women13
controller.add_product("Air Flash", 4800, "Women",
    {
        "Pink": [100, "S"],
        "Pink": [100, "M"],
        "Pink": [100, "L"],
        "Navy blue": [70, "S"],
        "Navy blue": [70, "M"],
        "Navy blue": [70, "L"],
        "Black": [80, "S"],
        "Black": [80, "M"],
        "Black": [80, "L"],
    }
)
#Women14
controller.add_product("Novel Min 00", 4000, "Women",
    {
        "Colorful": [70, "S"],
        "Colorful": [70, "M"],
        "Colorful": [70, "L"],
        "Blue": [100, "S"],
        "Blue": [100, "M"],
        "Blue": [100, "L"],
        "Pink": [80, "S"],
        "Pink": [80, "M"],
        "Pink": [80, "L"],
    }
)
#Kids1
controller.add_product("Air Mid Sum 4 ", 2700, "Kids",
    {
        "Blue": [100, "S"],
        "Blue": [100, "M"],
        "Blue": [100, "L"],
        "Colorful": [70, "S"],
        "Colorful": [70, "M"],
        "Colorful": [70, "L"],
        "Red": [80, "S"],
        "Red": [80, "M"],
        "Red": [80, "L"],
    }
)
#Kids2
controller.add_product(" Air Max 07", 3000, "Kids",
    {
        "Purple": [60, "S"],
        "Purple": [60, "M"],
        "Purple": [60, "L"],
        "Black": [80, "S"],
        "Black": [80, "M"],
        "Black": [80, "L"],
        "Orange": [80, "S"],
        "Orange": [80, "M"],
        "Orange": [80, "L"],
    }
)
#Kids3
controller.add_product("Lune Plus", 3500, "Kids",
    {
        "Neon": [60, "S"],
        "Neon": [60, "M"],
        "Neon": [60, "L"],
        "Azure": [70, "S"],
        "Azure": [70, "M"],
        "Azure": [70, "L"],
        "Black": [80, "S"],
        "Black": [80, "M"],
        "Black": [80, "L"],
    }
)
#Kids4
controller.add_product("Air G Cut", 3900, "Kids",
    {
        "Black": [70, "S"],
        "Black": [70, "M"],
        "Black": [70, "L"],
        "Pink": [80, "S"],
        "Pink": [80, "M"],
        "Pink": [80, "L"],
        "Orange": [50, "S"],
        "Orange": [50, "M"],
        "Orange": [50, "L"],
    }
)
#Kids5
controller.add_product("Air Max 27'0", 4200, "Kids",
    {
        "Pink": [100, "S"],
        "Pink": [100, "M"],
        "Pink": [100, "L"],
        "Blue": [80, "S"],
        "Blue": [80, "M"],
        "Blue": [80, "L"],
        "Green": [150, "S"],
        "Green": [150, "M"],
        "Green": [150, "L"],
    }
)
#Kids6
controller.add_product("Nike Air Max 07'", 2900, "Kids",
    {
        "Purple": [100, "S"],
        "Purple": [100, "M"],
        "Purple": [100, "L"],
        "Galaxy": [80, "S"],
        "Galaxy": [80, "M"],
        "Galaxy": [80, "L"],
        "Black": [70, "S"],
        "Black": [70, "M"],
        "Black": [70, "L"],
    }
)
#Kids7
controller.add_product("Nike Husky", 2100, "Kids",
    {
        "White": [100, "S"],
        "White": [100, "M"],
        "White": [100, "L"],
        "Red": [80, "S"],
        "Red": [80, "M"],
        "Red": [80, "L"],
        "Blue": [100, "S"],
        "Blue": [100, "M"],
        "Blue": [100, "L"],
    }
)
#Kids8
controller.add_product("Nike Blast 77-7", 2700, "Kids",
    {
        "Black": [70, "S"],
        "Black": [70, "M"],
        "Black": [70, "L"],
        "White": [90, "S"],
        "White": [90, "M"],
        "White": [90, "L"],
        "Honey": [80, "S"],
        "Honey": [80, "M"],
        "Honey": [80, "L"],
    }
)
#Kids9
controller.add_product("Nike Fire Plus", 1900, "Kids",
    {
        "Blue": [80, "S"],
        "Blue": [80, "M"],
        "Blue": [80, "L"],
        "Colorful": [70, "S"],
        "Colorful": [70, "M"],
        "Colorful": [70, "L"],
        "Grey": [100, "S"],
        "Grey": [100, "M"],
        "Grey": [100, "L"],
    }
)
#Kids10
controller.add_product("Air Inmortal 00", 2500, "Kids",
    {
        "Orange": [60, "S"],
        "Orange": [60, "M"],
        "Orange": [60, "L"],
        "White": [90, "S"],
        "White": [90, "M"],
        "White": [90, "L"],
        "Black": [80, "S"],
        "Black": [80, "M"],
        "Black": [80, "L"],
    }
)
#Kids11
controller.add_product("Novel Dream SP", 2200, "Kids",
    {
        "Mint": [50, "S"],
        "Mint": [50, "M"],
        "Mint": [50, "L"],
        "Red": [80, "S"],
        "Red": [80, "M"],
        "Red": [80, "L"],
        "White": [100, "S"],
        "White": [100, "M"],
        "White": [100, "L"],
    }
)
#Kids12
controller.add_product("Nike Tataui 03", 3100, "Kids",
    {
        "Brown": [50, "S"],
        "Brown": [50, "M"],
        "Brown": [50, "L"],
        "Colorful": [70, "S"],
        "Colorful": [70, "M"],
        "Colorful": [70, "L"],
        "Grey": [100, "S"],
        "Grey": [100, "M"],
        "Grey": [100, "L"],
    }
)

class ProductIn(BaseModel):
    name: str
    price: int
    gender: str
    style : dict

@router.get("/product-detail/{product_id}", tags =["Product"]) 
def get_product_detail(product_id : int):
    return controller.search_product_by_id(product_id)

@router.get("/product-category/{category}", tags =["Product"]) 
def get_product_in_category(category : str):
    return controller.search_product_in_category(category)

@router.delete("/product-delete/{product_id}", tags =["Admin"])
def delete_product(product_id : int):
    return controller.delete_product(product_id)

@router.post("/product-add/", tags =["Admin"])
async def add_product(data: ProductIn):
    return controller.add_product(data.name, data.price, data.gender, data.style)

@router.get("/product/{product_name}", tags =["Product"]) 
def get_product(product_name : str):
    return controller.search_product_by_name(product_name)