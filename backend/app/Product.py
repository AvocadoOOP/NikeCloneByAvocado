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
        "Blue": [50, "S"],
        "Blue": [50, "M"],
        "Blue": [50, "L"],
        "Orange": [80, "S"],
        "Orange": [80, "M"],
        "Orange": [80, "L"],
    }
    ,[
        {
            "name" : "Black",
            "list_images" :[    
                "PictureForNike/air-force-1-07.png",
                "PictureForNike/air-force-1-07-black-1.png",
                "PictureForNike/air-force-1-07-black-2.png",
                "PictureForNike/air-force-1-07-black-3.png",
                "PictureForNike/air-force-1-07-black-4.png",
                "PictureForNike/air-force-1-07-black-5.jpg",
                "PictureForNike/air-force-1-07-black-6.jpg"]
        }
        ,{
            "name" : "Blue",
            "list_images" : [    
                "PictureForNike/air-force-1-07-Blue-1.png",
                "PictureForNike/air-force-1-07-Blue-2.png",
                "PictureForNike/air-force-1-07-Blue-3.png",
                "PictureForNike/air-force-1-07-Blue-4.png",
                "PictureForNike/air-force-1-07-Blue-5.jpg",
                "PictureForNike/air-force-1-07-Blue-6.jpg"]
        },{
            "name" : "Orange",
            "list_images" : [    
                "PictureForNike/air-force-1-07-Orange-1.png",
                "PictureForNike/air-force-1-07-Orange-2.png",
                "PictureForNike/air-force-1-07-Orange-3.png",
                "PictureForNike/air-force-1-07-Orange-4.png",
                "PictureForNike/air-force-1-07-Orange-5.png",
                "PictureForNike/air-force-1-07-Orange-6.png"]
        }
    ]
)
#Men2
controller.add_product("Nike Full Fox", 4500, "Men",
    {
        "Grey": [50, "S"],
        "Grey": [50, "M"],
        "Grey": [50, "L"],
        "Red": [80, "S"],
        "Red": [80, "M"],
        "Red": [80, "L"],
        "Yellow": [50, "S"],
        "Yellow": [50, "M"],
        "Yellow": [50, "L"],
    }
    ,[
        {
            "name" : "Grey",
            "list_images" :[    
                "PictureForNike/Full-Fox.png",
                "PictureForNike/Full-Fox-Gray-1.png",
                "PictureForNike/Full-Fox-Gray-2.png",
                "PictureForNike/Full-Fox-Gray-3.png",
                "PictureForNike/Full-Fox-Gray-4.png",
                "PictureForNike/Full-Fox-Gray-5.jpg",
                "PictureForNike/Full-Fox-Gray-6.jpg"]
        }
        ,{
            "name" : "Red",
            "list_images" : [    
                "PictureForNike/Full-Fox-Red-1.png",
                "PictureForNike/Full-Fox-Red-2.png",
                "PictureForNike/Full-Fox-Red-3.png",
                "PictureForNike/Full-Fox-Red-4.png",
                "PictureForNike/Full-Fox-Red-5.jpg",
                "PictureForNike/Full-Fox-Red-6.jpg"]
        }
        ,{
            "name" : "Yellow",
            "list_images" : [    
                "PictureForNike/Full-Fox-Yellow-1.png",
                "PictureForNike/Full-Fox-Yellow-2.png",
                "PictureForNike/Full-Fox-Yellow-3.png",
                "PictureForNike/Full-Fox-Yellow-4.png",
                "PictureForNike/Full-Fox-Yellow-5.png",
                "PictureForNike/Full-Fox-Yellow-6.png"]
        }
    ]
)

#Men3
controller.add_product("Nike Air Jojo", 4200, "Men",
    {
        "Purple": [100, "S"],
        "Purple": [100, "M"],
        "Purple": [100, "L"],
        "Grey": [100, "S"],
        "Grey": [100, "M"],
        "Grey": [100, "L"],
        "White": [100, "S"],
        "White": [100, "M"],
        "White": [100, "L"],
    }
    ,[
        {
            "name" : "Purple",
            "list_images" :[    
                "PictureForNike/air-jojo.png",
                "PictureForNike/air-jojo-Purple-1.jpg",
                "PictureForNike/air-jojo-Purple-2.png",
                "PictureForNike/air-jojo-Purple-3.jpg",
                "PictureForNike/air-jojo-Purple-4.png",
                "PictureForNike/air-jojo-Purple-5.png",
                "PictureForNike/air-jojo-Purple-6.png"]
        }
        ,{
            "name" : "Grey",
            "list_images" : [    
                "PictureForNike/air-jojo-Grey-1.jpg",
                "PictureForNike/air-jojo-Grey-2.png",
                "PictureForNike/air-jojo-Grey-3.png",
                "PictureForNike/air-jojo-Grey-4.jpg",
                "PictureForNike/air-jojo-Grey-5.png",
                "PictureForNike/air-jojo-Grey-6.png"]
        }
        ,{
            "name" : "White",
            "list_images" : [    
                "PictureForNike/Air-Jojo-White-1.png",
                "PictureForNike/Air-Jojo-White-2.png",
                "PictureForNike/Air-Jojo-White-3.png",
                "PictureForNike/Air-Jojo-White-4.png",
                "PictureForNike/Air-Jojo-White-5.png",
                "PictureForNike/Air-Jojo-White-6.png"]
        }
    ]
)
#Men4
controller.add_product("Nike Air Popcorn 4", 5000, "Men",
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
    ,[
        {
            "name" : "Black",
            "list_images" :[    
                "PictureForNike/Air-Popcorn-4.png",
                "PictureForNike/Air-Popcorn-4-Black-1.png",
                "PictureForNike/Air-Popcorn-4-Black-2.png",
                "PictureForNike/Air-Popcorn-4-Black-3.png",
                "PictureForNike/Air-Popcorn-4-Black-4.png",
                "PictureForNike/Air-Popcorn-4-Black-5.jfif",
                "PictureForNike/Air-Popcorn-4-Black-6.png"]
        }
        ,{
            "name" : "Mint",
            "list_images" : [    
                "PictureForNike/Air-Popcorn-4-Mint-1.png",
                "PictureForNike/Air-Popcorn-4-Mint-2.png",
                "PictureForNike/Air-Popcorn-4-Mint-3.png",
                "PictureForNike/Air-Popcorn-4-Mint-4.jpg",
                "PictureForNike/Air-Popcorn-4-Mint-5.png",
                "PictureForNike/Air-Popcorn-4-Mint-6.png"]
        }
        ,{
            "name" : "Pink",
            "list_images" : [    
                "PictureForNike/Air-Popcorn-4-Pink-1.png",
                "PictureForNike/Air-Popcorn-4-Pink-2.png",
                "PictureForNike/Air-Popcorn-4-Pink-3.png",
                "PictureForNike/Air-Popcorn-4-Pink-4.png",
                "PictureForNike/Air-Popcorn-4-Pink-5.jfif",
                "PictureForNike/Air-Popcorn-4-Pink-6.png"]
        }
    ]
)
#Men5
controller.add_product("Nike Air Popcorn 9 By Me", 6100, "Men",
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
    ,[
        {
            "name" : "Brown",
            "list_images" :[    
                "PictureForNike/Air-Popcorn-9-By-Me.png",
                "PictureForNike/Air-Popcorn-9-By-Me-Brown-1.png",
                "PictureForNike/Air-Popcorn-9-By-Me-Brown-2.png",
                "PictureForNike/Air-Popcorn-9-By-Me-Brown-3.png",
                "PictureForNike/Air-Popcorn-9-By-Me-Brown-4.png",
                "PictureForNike/Air-Popcorn-9-By-Me-Brown-5.png",
                "PictureForNike/Air-Popcorn-9-By-Me-Brown-6.png"]
        }
        ,{
            "name" : "Red",
            "list_images" : [    
                "PictureForNike/Air-Popcorn-9-By-Me-Red-1.png",
                "PictureForNike/Air-Popcorn-9-By-Me-Red-2.png",
                "PictureForNike/Air-Popcorn-9-By-Me-Red-3.png",
                "PictureForNike/Air-Popcorn-9-By-Me-Red-4.png",
                "PictureForNike/Air-Popcorn-9-By-Me-Red-5.png",
                "PictureForNike/Air-Popcorn-9-By-Me-Red-6.png"]
        }
        ,{
            "name" : "Green",
            "list_images" : [    
                "PictureForNike/Air-Popcorn-9-By-Me-Green-1.png",
                "PictureForNike/Air-Popcorn-9-By-Me-Green-2.jfif",
                "PictureForNike/Air-Popcorn-9-By-Me-Green-3.jfif",
                "PictureForNike/Air-Popcorn-9-By-Me-Green-4.png",
                "PictureForNike/Air-Popcorn-9-By-Me-Green-5.png",
                "PictureForNike/Air-Popcorn-9-By-Me-Green-6.png"]
        }
    ]
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
    ,[
        {
            "name" : "Aquamarine",
            "list_images" :[    
                "PictureForNike/Taba.png",
                "PictureForNike/Taba-Aquamarine-1.png",
                "PictureForNike/Taba-Aquamarine-2.jfif",
                "PictureForNike/Taba-Aquamarine-3.png",
                "PictureForNike/Taba-Aquamarine-4.png",
                "PictureForNike/Taba-Aquamarine-5.png",
                "PictureForNike/Taba-Aquamarine-6.jfif"]
        }
        ,{
            "name" : "Lime",
            "list_images" : [    
                "PictureForNike/Taba-Lime-1.png",
                "PictureForNike/Taba-Lime-2.png",
                "PictureForNike/Taba-Lime-3.png",
                "PictureForNike/Taba-Lime-4.jpg",
                "PictureForNike/Taba-Lime-5.png",
                "PictureForNike/Taba-Lime-6.png"]
        }
        ,{
            "name" : "Black",
            "list_images" : [    
                "PictureForNike/Taba-Black-1.png",
                "PictureForNike/Taba-Black-2.png",
                "PictureForNike/Taba-Black-3.png",
                "PictureForNike/Taba-Black-4.png",
                "PictureForNike/Taba-Black-5.jfif",
                "PictureForNike/Taba-Black-6.png"]
        }
    ]
)
#Men7
controller.add_product("Nike Sum Vanom", 4500, "Men",
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
    ,[
        {
            "name" : "Green",
            "list_images" :[    
                "PictureForNike/Sum-Vanom.png",
                "PictureForNike/Sum-Vanom-Green-1.png",
                "PictureForNike/Sum-Vanom-Green-2.jfif",
                "PictureForNike/Sum-Vanom-Green-3.png",
                "PictureForNike/Sum-Vanom-Green-4.png",
                "PictureForNike/Sum-Vanom-Green-5.jfif",
                "PictureForNike/Sum-Vanom-Green-6.png"]
        }
        ,{
            "name" : "Blue",
            "list_images" : [    
                "PictureForNike/Sum-Vanom-Blue-1.png",
                "PictureForNike/Sum-Vanom-Blue-2.png",
                "PictureForNike/Sum-Vanom-Blue-3.png",
                "PictureForNike/Sum-Vanom-Blue-4.jpg",
                "PictureForNike/Sum-Vanom-Blue-5.png",
                "PictureForNike/Sum-Vanom-Blue-6.png"]
        }
        ,{
            "name" : "Black",
            "list_images" : [    
                "PictureForNike/Sum-Vanom-Black-1.png",
                "PictureForNike/Sum-Vanom-Black-2.jfif",
                "PictureForNike/Sum-Vanom-Black-3.png",
                "PictureForNike/Sum-Vanom-Black-4.png",
                "PictureForNike/Sum-Vanom-Black-5.jfif",
                "PictureForNike/Sum-Vanom-Black-6.png"]
        }
    ]
)
#Men8
controller.add_product("Nike Min Drift", 7000, "Men",
    {
        "Red": [60, "S"],
        "Red": [60, "M"],
        "Red": [60, "L"],
        "White": [100, "S"],
        "White": [100, "M"],
        "White": [100, "L"],
        "Green": [50, "S"],
        "Green": [50, "M"],
        "Green": [50, "L"],
    }
    ,[
        {
            "name" : "Red",
            "list_images" :[    
                "PictureForNike/Min-Drift.png",
                "PictureForNike/Min-Drift-Red-1.png",
                "PictureForNike/Min-Drift-Red-2.png",
                "PictureForNike/Min-Drift-Red-3.png",
                "PictureForNike/Min-Drift-Red-4.png",
                "PictureForNike/Min-Drift-Red-5.png",
                "PictureForNike/Min-Drift-Red-6.png"]
        }
        ,{
            "name" : "White",
            "list_images" : [    
                "PictureForNike/Min-Drift-White-1.png",
                "PictureForNike/Min-Drift-White-2.jfif",
                "PictureForNike/Min-Drift-White-3.png",
                "PictureForNike/Min-Drift-White-4.png",
                "PictureForNike/Min-Drift-White-5.png",
                "PictureForNike/Min-Drift-White-6.png"]
        }
        ,{
            "name" : "Green",
            "list_images" : [    
                "PictureForNike/Min-Drift-Black-1.png",
                "PictureForNike/Min-Drift-Black-2.jfif",
                "PictureForNike/Min-Drift-Black-3.png",
                "PictureForNike/Min-Drift-Black-4.png",
                "PictureForNike/Min-Drift-Black-5.png",
                "PictureForNike/Min-Drift-Black-6.png"]
        }
    ]
)
#Men9
controller.add_product("Nike Air Max 80", 6500, "Men",
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
    ,[
        {
            "name" : "Navy blue",
            "list_images" :[    
                "PictureForNike/Air-Max-80.png",
                "PictureForNike/Air-Max-80-Navy-blue-1.png",
                "PictureForNike/Air-Max-80-Navy-blue-2.jfif",
                "PictureForNike/Air-Max-80-Navy-blue-3.png",
                "PictureForNike/Air-Max-80-Navy-blue-4.png",
                "PictureForNike/Air-Max-80-Navy-blue-5.jfif",
                "PictureForNike/Air-Max-80-Navy-blue-6.jfif"]
        }
        ,{
            "name" : "Blue",
            "list_images" : [    
                "PictureForNike/Air-Max-80-Blue-1.png",
                "PictureForNike/Air-Max-80-Blue-2.png",
                "PictureForNike/Air-Max-80-Blue-3.png",
                "PictureForNike/Air-Max-80-Blue-4.png",
                "PictureForNike/Air-Max-80-Blue-5.png",
                "PictureForNike/Air-Max-80-Blue-6.png"]
        }
        ,{
            "name" : "Green",
            "list_images" : [    
                "PictureForNike/Air-Max-80-Navy-Green-1.png",
                "PictureForNike/Air-Max-80-Navy-Green-2.png",
                "PictureForNike/Air-Max-80-Navy-Green-3.png",
                "PictureForNike/Air-Max-80-Navy-Green-4.png",
                "PictureForNike/Air-Max-80-Navy-Green-5.png",
                "PictureForNike/Air-Max-80-Navy-Green-6.jfif"]
        }
    ]
)
#Men10
controller.add_product("Nike Hard OOP 4", 100000, "Men",
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
    ,[
        {
            "name" : "Lime",
            "list_images" :[    
                "PictureForNike/Hard-OOP-4.png",
                "PictureForNike/Hard-OOP-4-Lime-1.png",
                "PictureForNike/Hard-OOP-4-Lime-2.png",
                "PictureForNike/Hard-OOP-4-Lime-3.png",
                "PictureForNike/Hard-OOP-4-Lime-4.png",
                "PictureForNike/Hard-OOP-4-Lime-5.png",
                "PictureForNike/Hard-OOP-4-Lime-6.png"]
        }
        ,{
            "name" : "Grey",
            "list_images" : [    
                "PictureForNike/Hard-OOP-4-Grey-1.png",
                "PictureForNike/Hard-OOP-4-Grey-2.png",
                "PictureForNike/Hard-OOP-4-Grey-3.png",
                "PictureForNike/Hard-OOP-4-Grey-4.png",
                "PictureForNike/Hard-OOP-4-Grey-5.png",
                "PictureForNike/Hard-OOP-4-Grey-6.png"]
        }
        ,{
            "name" : "Black",
            "list_images" : [    
                "PictureForNike/Hard-OOP-4-Black-1.png",
                "PictureForNike/Hard-OOP-4-Black-2.png",
                "PictureForNike/Hard-OOP-4-Black-3.png",
                "PictureForNike/Hard-OOP-4-Black-4.png",
                "PictureForNike/Hard-OOP-4-Black-5.jfif",
                "PictureForNike/Hard-OOP-4-Black-6.png"]
        }
    ]
)
#Men11
controller.add_product("Nike Air Max 27", 6400, "Men",
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
    ,[
        {
            "name" : "Orange",
            "list_images" :[    
                "PictureForNike/Air-Max-27.png",
                "PictureForNike/Air-Max-27-Orange-1.png",
                "PictureForNike/Air-Max-27-Orange-2.png",
                "PictureForNike/Air-Max-27-Orange-3.png",
                "PictureForNike/Air-Max-27-Orange-4.png",
                "PictureForNike/Air-Max-27-Orange-5.png",
                "PictureForNike/Air-Max-27-Orange-6.png"]
        }
        ,{
            "name" : "Purple",
            "list_images" : [    
                "PictureForNike/Air-Max-27-Purple-1.jfif",
                "PictureForNike/Air-Max-27-Purple-2.jfif",
                "PictureForNike/Air-Max-27-Purple-3.jfif",
                "PictureForNike/Air-Max-27-Purple-4.png",
                "PictureForNike/Air-Max-27-Purple-5.jfif",
                "PictureForNike/Air-Max-27-Purple-6.png"]
        }
        ,{
            "name" : "Pink",
            "list_images" : [    
                "PictureForNike/Air-Max-27-Pink-1.png",
                "PictureForNike/Air-Max-27-Pink-2.png",
                "PictureForNike/Air-Max-27-Pink-3.png",
                "PictureForNike/Air-Max-27-Pink-4.png",
                "PictureForNike/Air-Max-27-Pink-5.png",
                "PictureForNike/Air-Max-27-Pink-6.png"]
        }
    ]
)
#Men12
controller.add_product("Nike Air Max Hippo", 5600, "Men",
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
    ,[
        {
            "name" : "Cyan",
            "list_images" :[    
                "PictureForNike/Air-Max-Hippo.png",
                "PictureForNike/Air-Max-Hippo-Cyan-1.jfif",
                "PictureForNike/Air-Max-Hippo-Cyan-2.jfif",
                "PictureForNike/Air-Max-Hippo-Cyan-3.png",
                "PictureForNike/Air-Max-Hippo-Cyan-4.png",
                "PictureForNike/Air-Max-Hippo-Cyan-5.jfif",
                "PictureForNike/Air-Max-Hippo-Cyan-6.jfif"]
        }
        ,{
            "name" : "Black",
            "list_images" : [    
                "PictureForNike/Air-Max-Hippo-Black-1.jfif",
                "PictureForNike/Air-Max-Hippo-Black-2.jfif",
                "PictureForNike/Air-Max-Hippo-Black-3.jfif",
                "PictureForNike/Air-Max-Hippo-Black-4.png",
                "PictureForNike/Air-Max-Hippo-Black-5.jfif",
                "PictureForNike/Air-Max-Hippo-Black-6.jfif"]
        }
        ,{
            "name" : "Green",
            "list_images" : [    
                "PictureForNike/Air-Max-Hippo-Green-1.png",
                "PictureForNike/Air-Max-Hippo-Green-2.png",
                "PictureForNike/Air-Max-Hippo-Green-3.png",
                "PictureForNike/Air-Max-Hippo-Green-4.png",
                "PictureForNike/Air-Max-Hippo-Green-5.jfif",
                "PictureForNike/Air-Max-Hippo-Green-6.png"]
        }
    ]
)
#Men13
controller.add_product("Nike Air Luk", 7800, "Men",
    {
        "Galaxy": [100, "S"],
        "Galaxy": [100, "M"],
        "Galaxy": [100, "L"],
        "Blue": [50, "S"],
        "Blue": [50, "M"],
        "Blue": [50, "L"],
        "White": [50, "S"],
        "White": [50, "M"],
        "White": [50, "L"],
    }
    ,[
        {
            "name" : "Galaxy",
            "list_images" :[    
                "PictureForNike/Air-Luk.png",
                "PictureForNike/Air-Luk-Galaxy-1.jfif",
                "PictureForNike/Air-Luk-Galaxy-2.jfif",
                "PictureForNike/Air-Luk-Galaxy-3.png",
                "PictureForNike/Air-Luk-Galaxy-4.png",
                "PictureForNike/Air-Luk-Galaxy-5.jfif",
                "PictureForNike/Air-Luk-Galaxy-6.jfif"]
        }
        ,{
            "name" : "Blue",
            "list_images" : [    
                "PictureForNike/Air-Luk-Blue-1.jfif",
                "PictureForNike/Air-Luk-Blue-2.jfif",
                "PictureForNike/Air-Luk-Blue-3.png",
                "PictureForNike/Air-Luk-Blue-4.png",
                "PictureForNike/Air-Luk-Blue-5.png",
                "PictureForNike/Air-Luk-Blue-6.png"]
        }
        ,{
            "name" : "White",
            "list_images" : [    
                "PictureForNike/Air-Luk-White-1.png",
                "PictureForNike/Air-Luk-White-2.png",
                "PictureForNike/Air-Luk-White-3.png",
                "PictureForNike/Air-Luk-White-4.png",
                "PictureForNike/Air-Luk-White-5.png",
                "PictureForNike/Air-Luk-White-6.png"]
        }
    ]
)
#Men14
controller.add_product("Nike Y2K Men 01", 5700, "Men",
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
    ,[
        {
            "name" : "Brown",
            "list_images" :[    
                "PictureForNike/Y2K-Men-01.png",
                "PictureForNike/Y2K-Men-01-Brown-1.jfif",
                "PictureForNike/Y2K-Men-01-Brown-2.jfif",
                "PictureForNike/Y2K-Men-01-Brown-3.png",
                "PictureForNike/Y2K-Men-01-Brown-4.png",
                "PictureForNike/Y2K-Men-01-Brown-5.jfif",
                "PictureForNike/Y2K-Men-01-Brown-6.jfif"]
        }
        ,{
            "name" : "Blue",
            "list_images" : [    
                "PictureForNike/Y2K-Men-01-Blue-1.png",
                "PictureForNike/Y2K-Men-01-Blue-2.jfif",
                "PictureForNike/Y2K-Men-01-Blue-3.png",
                "PictureForNike/Y2K-Men-01-Blue-4.png",
                "PictureForNike/Y2K-Men-01-Blue-5.png",
                "PictureForNike/Y2K-Men-01-Blue-6.png"]
        }
        ,{
            "name" : "Black",
            "list_images" : [    
                "PictureForNike/Y2K-Men-01-Black-1.png",
                "PictureForNike/Y2K-Men-01-Black-2.jfif",
                "PictureForNike/Y2K-Men-01-Black-3.png",
                "PictureForNike/Y2K-Men-01-Black-4.png",
                "PictureForNike/Y2K-Men-01-Black-5.jfif",
                "PictureForNike/Y2K-Men-01-Black-6.png"]
        }
    ]
)
#Men15
controller.add_product("Nike Air Shell 70", 4000, "Men",
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
    ,[
        {
            "name" : "Pink",
            "list_images" :[    
                "PictureForNike/Air-Shell-70.png",
                "PictureForNike/Air-Shell-70-Pink-1.png",
                "PictureForNike/Air-Shell-70-Pink-2.png",
                "PictureForNike/Air-Shell-70-Pink-3.png",
                "PictureForNike/Air-Shell-70-Pink-4.png",
                "PictureForNike/Air-Shell-70-Pink-5.png",
                "PictureForNike/Air-Shell-70-Pink-6.png"]
        }
        ,{
            "name" : "Green",
            "list_images" : [    
                "PictureForNike/Air-Shell-70-Green-1.png",
                "PictureForNike/Air-Shell-70-Green-2.jfif",
                "PictureForNike/Air-Shell-70-Green-3.png",
                "PictureForNike/Air-Shell-70-Green-4.png",
                "PictureForNike/Air-Shell-70-Green-5.jfif",
                "PictureForNike/Air-Shell-70-Green-6.jfif"]
        }
        ,{
            "name" : "Orange",
            "list_images" : [    
                "PictureForNike/Air-Shell-70-Orange-1.png",
                "PictureForNike/Air-Shell-70-Orange-2.png",
                "PictureForNike/Air-Shell-70-Orange-3.png",
                "PictureForNike/Air-Shell-70-Orange-4.png",
                "PictureForNike/Air-Shell-70-Orange-5.png",
                "PictureForNike/Air-Shell-70-Orange-6.png"]
        }
    ]
)
#Women1
controller.add_product("Nike Taba", 4400, "Women",
    {
        "Puce": [50, "S"],
        "Puce": [50, "M"],
        "Puce": [50, "L"],
        "Black": [100, "S"],
        "Black": [100, "M"],
        "Black": [100, "L"],
        "Mint": [50, "S"],
        "Mint": [50, "M"],
        "Mint": [50, "L"],
    }
    ,[
        {
            "name" : "Puce",
            "list_images" : [   
                "PictureForNike/taba.png", 
                "PictureForNike/taba-Puce-1.jpg",
                "PictureForNike/taba-Puce-2.jpg",
                "PictureForNike/taba-Puce-3.jpg",
                "PictureForNike/taba-Puce-4.jpg",
                "PictureForNike/taba-Puce-5.jpg",
                "PictureForNike/taba-Puce-6.jpg"]
        }
        ,{
            "name" : "Black",
            "list_images" :[    
                "PictureForNike/taba-Black-1.jpg",
                "PictureForNike/taba-Black-2.jpg",
                "PictureForNike/taba-Black-3.jpg",
                "PictureForNike/taba-Black-4.jpg",
                "PictureForNike/taba-Black-5.jpg",
                "PictureForNike/taba-Black-6.jpg"]
        },{
           "name" : "Mint",
            "list_images" : [    
                "PictureForNike/taba-mint-1.jpg",
                "PictureForNike/taba-mint-2.jpg",
                "PictureForNike/taba-mint-3.jpg",
                "PictureForNike/taba-mint-4.jpg",
                "PictureForNike/taba-mint-5.jpg",
                "PictureForNike/taba-mint-6.jpg"]
        }
    ]     
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
    ,[
        {
            "name" : "Black",
            "list_images" : [   
                "PictureForNike/Air-Force-1-09-Black.png", 
                "PictureForNike/Air-Force-1-09-Black-1.png",
                "PictureForNike/Air-Force-1-09-Black-2.png",
                "PictureForNike/Air-Force-1-09-Black-3.png",
                "PictureForNike/Air-Force-1-09-Black-4.png",
                "PictureForNike/Air-Force-1-09-Black-5.png",
                "PictureForNike/Air-Force-1-09-Black-6.png"]
        }
        ,{
            "name" : "Brown",
            "list_images" :[    
                "PictureForNike/Air-Force-1-09-Brown-1.png",
                "PictureForNike/Air-Force-1-09-Brown-2.png",
                "PictureForNike/Air-Force-1-09-Brown-3.png",
                "PictureForNike/Air-Force-1-09-Brown-4.png",
                "PictureForNike/Air-Force-1-09-Brown-5.png",
                "PictureForNike/Air-Force-1-09-Brown-6.png"]
        },{
           "name" : "Pink",
            "list_images" : [    
                "PictureForNike/Air-Force-1-09-Pink-1.png",
                "PictureForNike/Air-Force-1-09-Pink-2.png",
                "PictureForNike/Air-Force-1-09-Pink-3.png",
                "PictureForNike/Air-Force-1-09-Pink-4.png",
                "PictureForNike/Air-Force-1-09-Pink-5.png",
                "PictureForNike/Air-Force-1-09-Pink-6.png"]
        }
    ]     
)
#Women3
controller.add_product("Nike Princess 19", 5500, "Women",
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
    ,[
        {
            "name" : "Pink",
            "list_images" : [    
                "PictureForNike/princess-19.png",
                "PictureForNike/princess-19-Pink-1.png",
                "PictureForNike/princess-19-Pink-2.png",
                "PictureForNike/princess-19-Pink-3.png",
                "PictureForNike/princess-19-Pink-4.png",
                "PictureForNike/princess-19-Pink-5.png",
                "PictureForNike/princess-19-Pink-6.png"]
        }
        ,{
            "name" : "Black",
            "list_images" :[    
                "PictureForNike/princess-19-Black-1.png",
                "PictureForNike/princess-19-Black-2.png",
                "PictureForNike/princess-19-Black-3.png",
                "PictureForNike/princess-19-Black-4.png",
                "PictureForNike/princess-19-Black-5.png",
                "PictureForNike/princess-19-Black-6.png"]
        },{
           "name" : "Grey",
           "list_images" :[    
                "PictureForNike/princess-19-Grey-1.png",
                "PictureForNike/princess-19-Grey-2.png",
                "PictureForNike/princess-19-Grey-3.png",
                "PictureForNike/princess-19-Grey-4.png",
                "PictureForNike/princess-19-Grey-5.png",
                "PictureForNike/princess-19-Grey-6.png"]
        }
    ]
)
#Women4
controller.add_product("Nike Air Max 12", 4700, "Women",
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
     ,[
        {
            "name" : "Grey",
            "list_images" : [    
                "PictureForNike/Air-Max-12.png",
                "PictureForNike/Air-Max-12-Grey-1.png",
                "PictureForNike/Air-Max-12-Grey-2.png",
                "PictureForNike/Air-Max-12-Grey-3.png",
                "PictureForNike/Air-Max-12-Grey-4.png",
                "PictureForNike/Air-Max-12-Grey-5.png",
                "PictureForNike/Air-Max-12-Grey-6.png"]
        }
        ,{
            "name" : "Black",
            "list_images" :[    
                "PictureForNike/Air-Max-12-Black-1.png",
                "PictureForNike/Air-Max-12-Black-2.png",
                "PictureForNike/Air-Max-12-Black-3.png",
                "PictureForNike/Air-Max-12-Black-4.png",
                "PictureForNike/Air-Max-12-Black-5.png",
                "PictureForNike/Air-Max-12-Black-6.png"]
        },{
           "name" : "Purple",
           "list_images" :[    
                "PictureForNike/Air-Max-12-Purple-1.png",
                "PictureForNike/Air-Max-12-Purple-2.png",
                "PictureForNike/Air-Max-12-Purple-3.png",
                "PictureForNike/Air-Max-12-Purple-4.png",
                "PictureForNike/Air-Max-12-Purple-5.png",
                "PictureForNike/Air-Max-12-Purple-6.png"]
        }
    ]    
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
    ,[
        {
            "name" : "Mint",
            "list_images" : [    
                "PictureForNike/Pegasus-39.png",
                "PictureForNike/Pegasus-39-Mint-1.png",
                "PictureForNike/Pegasus-39-Mint-2.png",
                "PictureForNike/Pegasus-39-Mint-3.jfif",
                "PictureForNike/Pegasus-39-Mint-4.png",
                "PictureForNike/Pegasus-39-Mint-5.jfif",
                "PictureForNike/Pegasus-39-Mint-6.jfif"]
        }
        ,{
            "name" : "Pink",
            "list_images" :[    
                "PictureForNike/Pegasus-39-Pink-1.png",
                "PictureForNike/Pegasus-39-Pink-2.png",
                "PictureForNike/Pegasus-39-Pink-3.png",
                "PictureForNike/Pegasus-39-Pink-4.png",
                "PictureForNike/Pegasus-39-Pink-5.jfif",
                "PictureForNike/Pegasus-39-Pink-6.png"]
        },{
          "name" : "Black",
            "list_images" :[    
                "PictureForNike/Pegasus-39-Black-1.png",
                "PictureForNike/Pegasus-39-Black-2.jfif",
                "PictureForNike/Pegasus-39-Black-3.png",
                "PictureForNike/Pegasus-39-Black-4.png",
                "PictureForNike/Pegasus-39-Black-5.jfif",
                "PictureForNike/Pegasus-39-Black-6.png"]
        }
    ]    
)
#Women6
controller.add_product("Nike Air Vampire Max ", 7700, "Women",
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
    ,[
        {
            "name" : "Red",
            "list_images" : [    
                "PictureForNike/Air-Vampire-Max.png",
                "PictureForNike/Air-Vampire-Max-Red-1.jfif",
                "PictureForNike/Air-Vampire-Max-Red-2.jfif",
                "PictureForNike/Air-Vampire-Max-Red-3.png",
                "PictureForNike/Air-Vampire-Max-Red-4.png",
                "PictureForNike/Air-Vampire-Max-Red-5.jfif",
                "PictureForNike/Air-Vampire-Max-Red-6.jfif"]
        }
        ,{
            "name" : "Green",
            "list_images" :[    
                "PictureForNike/Air-Vampire-Max-Green-1.png",
                "PictureForNike/Air-Vampire-Max-Green-2.png",
                "PictureForNike/Air-Vampire-Max-Green-3.png",
                "PictureForNike/Air-Vampire-Max-Green-4.png",
                "PictureForNike/Air-Vampire-Max-Green-5.jfif",
                "PictureForNike/Air-Vampire-Max-Green-6.png"]
        },{
          "name" : "Black",
            "list_images" :[    
                "PictureForNike/Air-Vampire-Max-Black-1.png",
                "PictureForNike/Air-Vampire-Max-Black-2.jfif",
                "PictureForNike/Air-Vampire-Max-Black-3.png",
                "PictureForNike/Air-Vampire-Max-Black-4.png",
                "PictureForNike/Air-Vampire-Max-Black-5.jfif",
                "PictureForNike/Air-Vampire-Max-Black-6.jfif"]
        }
    ]    
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
    ,[
        {
            "name" : "Puce",
            "list_images" : [    
                "PictureForNike/Fura-Plus.png",
                "PictureForNike/Fura-Plus-Puce-1.png",
                "PictureForNike/Fura-Plus-Puce-2.png",
                "PictureForNike/Fura-Plus-Puce-3.png",
                "PictureForNike/Fura-Plus-Puce-4.png",
                "PictureForNike/Fura-Plus-Puce-5.jfif",
                "PictureForNike/Fura-Plus-Puce-6.jfif"]
        }
        ,{
            "name" : "Colorful",
            "list_images" :[    
                "PictureForNike/Fura-Plus-colorful-1.png",
                "PictureForNike/Fura-Plus-colorful-2.png",
                "PictureForNike/Fura-Plus-colorful-3.png",
                "PictureForNike/Fura-Plus-colorful-4.png",
                "PictureForNike/Fura-Plus-colorful-5.png",
                "PictureForNike/Fura-Plus-colorful-6.png"]
        },{
          "name" : "Orange",
            "list_images" :[    
                "PictureForNike/Fura-Plus-Orange-1.png",
                "PictureForNike/Fura-Plus-Orange-2.png",
                "PictureForNike/Fura-Plus-Orange-3.png",
                "PictureForNike/Fura-Plus-Orange-4.png",
                "PictureForNike/Fura-Plus-Orange-5.jfif",
                "PictureForNike/Fura-Plus-Orange-6.png"]
        }
    ]    
)
#Women8
controller.add_product("Nike Sum Vanom", 4200, "Women",
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
    ,[
        {
            "name" : "Green",
            "list_images" : [    
                "PictureForNike/Sum-Vanom.png",
                "PictureForNike/Sum-Vanom-Green-1.png",
                "PictureForNike/Sum-Vanom-Green-2.jfif",
                "PictureForNike/Sum-Vanom-Green-3.png",
                "PictureForNike/Sum-Vanom-Green-4.png",
                "PictureForNike/Sum-Vanom-Green-5.jfif",
                "PictureForNike/Sum-Vanom-Green-6.png"]
        }
        ,{
            "name" : "Blue",
            "list_images" :[    
                "PictureForNike/Fura-Plus-colorful-1.png",
                "PictureForNike/Fura-Plus-colorful-2.png",
                "PictureForNike/Fura-Plus-colorful-3.png",
                "PictureForNike/Fura-Plus-colorful-4.png",
                "PictureForNike/Fura-Plus-colorful-5.png",
                "PictureForNike/Fura-Plus-colorful-6.png"]
        },{
          "name" : "Black",
            "list_images" :[    
                "PictureForNike/Sum-Vanom-Black-1.png",
                "PictureForNike/Sum-Vanom-Black-2.jfif",
                "PictureForNike/Sum-Vanom-Black-3.png",
                "PictureForNike/Sum-Vanom-Black-4.png",
                "PictureForNike/Sum-Vanom-Black-5.jfif",
                "PictureForNike/Sum-Vanom-Black-6.png"]
        }
    ]    
)  
#Women9
controller.add_product("Nike Solo Max By Me", 3900, "Women",
    {
        "Pink": [70, "S"],
        "Pink": [70, "M"],
        "Pink": [70, "L"],
        "Cyan": [50, "S"],
        "Cyan": [50, "M"],
        "Cyan": [50, "L"],
        "Grey": [80, "S"],
        "Grey": [80, "M"],
        "Grey": [80, "L"],
    }
    ,[
        {
            "name" : "Pink",
            "list_images" : [    
                "PictureForNike/Solo-Max-By-Me.png",
                "PictureForNike/Solo-Max-By-Me-Pink-1.png",
                "PictureForNike/Solo-Max-By-Me-Pink-2.png",
                "PictureForNike/Solo-Max-By-Me-Pink-3.png",
                "PictureForNike/Solo-Max-By-Me-Pink-4.png",
                "PictureForNike/Solo-Max-By-Me-Pink-5.png",
                "PictureForNike/Solo-Max-By-Me-Pink-6.png"]
        }
        ,{
            "name" : "Cyan",
            "list_images" :[    
                "PictureForNike/Solo-Max-By-Me-Cyan-1.png",
                "PictureForNike/Solo-Max-By-Me-Cyan-2.png",
                "PictureForNike/Solo-Max-By-Me-Cyan-3.png",
                "PictureForNike/Solo-Max-By-Me-Cyan-4.png",
                "PictureForNike/Solo-Max-By-Me-Cyan-5.jfif",
                "PictureForNike/Solo-Max-By-Me-Cyan-6.png"]
        },{
          "name" : "Grey",
            "list_images" :[    
                "PictureForNike/Solo-Max-By-Me-Grey-1.png",
                "PictureForNike/Solo-Max-By-Me-Grey-2.png",
                "PictureForNike/Solo-Max-By-Me-Grey-3.png",
                "PictureForNike/Solo-Max-By-Me-Grey-4.png",
                "PictureForNike/Solo-Max-By-Me-Grey-5.png",
                "PictureForNike/Solo-Max-By-Me-Grey-6.png"]
        }
    ]    
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
    ,[
        {
            "name" : "Cyan",
            "list_images" : [    
                "PictureForNike/Revo-Hip.png",
                "PictureForNike/Revo-Hip-Cyan-1.png",
                "PictureForNike/Revo-Hip-Cyan-2.png",
                "PictureForNike/Revo-Hip-Cyan-3.png",
                "PictureForNike/Revo-Hip-Cyan-4.png",
                "PictureForNike/Revo-Hip-Cyan-5.jfif",
                "PictureForNike/Revo-Hip-Cyan-6.png"]
        }
        ,{
            "name" : "Pink",
            "list_images" :[    
                "PictureForNike/Revo-Hip-Pink-1.png",
                "PictureForNike/Revo-Hip-Pink-2.jfif",
                "PictureForNike/Revo-Hip-Pink-3.png",
                "PictureForNike/Revo-Hip-Pink-4.png",
                "PictureForNike/Revo-Hip-Pink-5.jfif",
                "PictureForNike/Revo-Hip-Pink-6.png"]
        },{
          "name" : "Black",
            "list_images" :[    
                "PictureForNike/Revo-Hip-Black-1.png",
                "PictureForNike/Revo-Hip-Black-2.jfif",
                "PictureForNike/Revo-Hip-Black-3.png",
                "PictureForNike/Revo-Hip-Black-4.png",
                "PictureForNike/Revo-Hip-Black-5.jfif",
                "PictureForNike/Revo-Hip-Black-6.png"]
        }
    ]    
)
#Women11
controller.add_product("Nike Air Zion Mood", 4700, "Women",
    {
        "Blue": [80, "S"],
        "Blue": [80, "M"],
        "Blue": [80, "L"],
        "White": [100, "S"],
        "White": [100, "M"],
        "White": [100, "L"],
        "Neon": [60, "S"],
        "Neon": [60, "M"],
        "Neon": [60, "L"],
    }
    ,[
        {
            "name" : "Blue",
            "list_images" : [    
                "PictureForNike/Air-Zion-Mood.png",
                "PictureForNike/Air-Zion-Mood-Blue-1.png",
                "PictureForNike/Air-Zion-Mood-Blue-2.jfif",
                "PictureForNike/Air-Zion-Mood-Blue-3.png",
                "PictureForNike/Air-Zion-Mood-Blue-4.png",
                "PictureForNike/Air-Zion-Mood-Blue-5.jfif",
                "PictureForNike/Air-Zion-Mood-Blue-6.png"]
        }
        ,{
            "name" : "White",
            "list_images" :[    
                "PictureForNike/Air-Zion-Mood-White-1.png",
                "PictureForNike/Air-Zion-Mood-White-2.jfif",
                "PictureForNike/Air-Zion-Mood-White-3.jfif",
                "PictureForNike/Air-Zion-Mood-White-4.png",
                "PictureForNike/Air-Zion-Mood-White-5.png",
                "PictureForNike/Air-Zion-Mood-White-6.png"]
        },{
          "name" : "Neon",
            "list_images" :[    
                "PictureForNike/Air-Zion-Mood-Neon-1.png",
                "PictureForNike/Air-Zion-Mood-Neon-2.png",
                "PictureForNike/Air-Zion-Mood-Neon-3.png",
                "PictureForNike/Air-Zion-Mood-Neon-4.png",
                "PictureForNike/Air-Zion-Mood-Neon-5.png",
                "PictureForNike/Air-Zion-Mood-Neon-6.png"]
        }
    ]    
)
#Women12
controller.add_product("Nike Area 51", 5100, "Women",
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
    ,[
        {
            "name" : "Purple",
            "list_images" : [    
                "PictureForNike/Area-51.png",
                "PictureForNike/Area-51-Purple-1.jfif",
                "PictureForNike/Area-51-Purple-2.jfif",
                "PictureForNike/Area-51-Purple-3.png",
                "PictureForNike/Area-51-Purple-4.jfif",
                "PictureForNike/Area-51-Purple-5.jfif",
                "PictureForNike/Area-51-Purple-6.jfif"]
        }
        ,{
            "name" : "Black",
            "list_images" :[    
                "PictureForNike/Area-51-Black-1.jfif",
                "PictureForNike/Area-51-Black-2.jfif",
                "PictureForNike/Area-51-Black-3.png",
                "PictureForNike/Area-51-Black-4.jfif",
                "PictureForNike/Area-51-Black-5.jfif",
                "PictureForNike/Area-51-Black-6.jfif"]
        },{
          "name" : "Colorful",
            "list_images" :[    
                "PictureForNike/Area-51-Colorful-1.png",
                "PictureForNike/Area-51-Colorful-2.png",
                "PictureForNike/Area-51-Colorful-3.jfif",
                "PictureForNike/Area-51-Colorful-4.png",
                "PictureForNike/Area-51-Colorful-5.png",
                "PictureForNike/Area-51-Colorful-6.jfif"]
        }
    ]    
)
#Women13
controller.add_product("Nike Air Flash", 4800, "Women",
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
    ,[
        {
            "name" : "Pink",
            "list_images" : [    
                "PictureForNike/Air-Flash.png",
                "PictureForNike/Air-Flash-Pink-1.png",
                "PictureForNike/Air-Flash-Pink-2.png",
                "PictureForNike/Air-Flash-Pink-3.png",
                "PictureForNike/Air-Flash-Pink-4.png",
                "PictureForNike/Air-Flash-Pink-5.jfif",
                "PictureForNike/Air-Flash-Pink-6.png"]
        }
        ,{
            "name" : "Navy blue",
            "list_images" :[    
                "PictureForNike/Air-Flash-Navy-Blue-1.jfif",
                "PictureForNike/Air-Flash-Navy-Blue-2.jfif",
                "PictureForNike/Air-Flash-Navy-Blue-3.jfif",
                "PictureForNike/Air-Flash-Navy-Blue-4.jfif",
                "PictureForNike/Air-Flash-Navy-Blue-5.jfif",
                "PictureForNike/Air-Flash-Navy-Blue-6.jfif"]
        },{
          "name" : "Black",
            "list_images" :[    
                "PictureForNike/Air-Flash-Black-1.jfif",
                "PictureForNike/Air-Flash-Black-2.jfif",
                "PictureForNike/Air-Flash-Black-3.jfif",
                "PictureForNike/Air-Flash-Black-4.png",
                "PictureForNike/Air-Flash-Black-5.jfif",
                "PictureForNike/Air-Flash-Black-6.jfif"]
        }
    ]    
)
#Women14
controller.add_product("Nike Novel Min 00", 4000, "Women",
    {
        "Blue": [100, "S"],
        "Blue": [100, "M"],
        "Blue": [100, "L"],
        "Colorful": [70, "S"],
        "Colorful": [70, "M"],
        "Colorful": [70, "L"],
        "Pink": [80, "S"],
        "Pink": [80, "M"],
        "Pink": [80, "L"],
    }
    ,[
        {
            "name" : "Blue",
            "list_images" : [    
                "PictureForNike/Novel-Min-00.png",
                "PictureForNike/Novel-Min-00-Blue-1.jfif",
                "PictureForNike/Novel-Min-00-Blue-2.png",
                "PictureForNike/Novel-Min-00-Blue-3.jfif",
                "PictureForNike/Novel-Min-00-Blue-4.png",
                "PictureForNike/Novel-Min-00-Blue-5.jfif",
                "PictureForNike/Novel-Min-00-Blue-6.jfif"]
        }
        ,{
            "name" : "Colorful",
            "list_images" :[    
                "PictureForNike/Novel-Min-00-Colorful-1.jfif",
                "PictureForNike/Novel-Min-00-Colorful-2.jfif",
                "PictureForNike/Novel-Min-00-Colorful-3.jfif",
                "PictureForNike/Novel-Min-00-Colorful-4.png",
                "PictureForNike/Novel-Min-00-Colorful-5.png",
                "PictureForNike/Novel-Min-00-Colorful-6.jfif"]
        },{
          "name" : "Pink",
            "list_images" :[    
                "PictureForNike/Novel-Min-00-Pink-1.png",
                "PictureForNike/Novel-Min-00-Pink-2.jfif",
                "PictureForNike/Novel-Min-00-Pink-3.png",
                "PictureForNike/Novel-Min-00-Pink-4.png",
                "PictureForNike/Novel-Min-00-Pink-5.jfif",
                "PictureForNike/Novel-Min-00-Pink-6.png"]
        }
    ]    
)
#Kids1
controller.add_product("Nike Air Mid Sum 4 ", 2700, "Kids",
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
    },[
        {
            "name" : "Blue",
            "list_images" :[    
                "PictureForNike/Air-Mid-Sum-4.png",
                "PictureForNike/Air-Mid-Sum-4-Blue-1.jfif",
                "PictureForNike/Air-Mid-Sum-4-Blue-2.png",
                "PictureForNike/Air-Mid-Sum-4-Blue-3.png",
                "PictureForNike/Air-Mid-Sum-4-Blue-4.jfif",
                "PictureForNike/Air-Mid-Sum-4-Blue-5.jfif",
                "PictureForNike/Air-Mid-Sum-4-Blue-6.jfif"]
        }
        ,{
            "name" : "Colorful",
            "list_images" : [    
                "PictureForNike/Air-Mid-Sum-4-Colorful-1.jfif",
                "PictureForNike/Air-Mid-Sum-4-Colorful-2.png",
                "PictureForNike/Air-Mid-Sum-4-Colorful-3.png",
                "PictureForNike/Air-Mid-Sum-4-Colorful-4.png",
                "PictureForNike/Air-Mid-Sum-4-Colorful-5.png",
                "PictureForNike/Air-Mid-Sum-4-Colorful-6.png"]
        },{
            "name" : "Red",
            "list_images" : [    
                "PictureForNike/Air-Mid-Sum-4-Red-1.jfif",
                "PictureForNike/Air-Mid-Sum-4-Red-2.png",
                "PictureForNike/Air-Mid-Sum-4-Red-3.png",
                "PictureForNike/Air-Mid-Sum-4-Red-4.jfif",
                "PictureForNike/Air-Mid-Sum-4-Red-5.png",
                "PictureForNike/Air-Mid-Sum-4-Red-6.png"]
        }
    ]
)
#Kids2
controller.add_product("Nike Air Max 07", 3000, "Kids",
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
    } ,[
        {
            "name" : "Purple",
            "list_images" :[    
                "PictureForNike/Air-Max-07.png",
                "PictureForNike/Air-Max-07-Purple-1.jfif",
                "PictureForNike/Air-Max-07-Purple-2.png",
                "PictureForNike/Air-Max-07-Purple-3.png",
                "PictureForNike/Air-Max-07-Purple-4.jfif",
                "PictureForNike/Air-Max-07-Purple-5.jfif",
                "PictureForNike/Air-Max-07-Purple-6.jfif"]
        }
        ,{
            "name" : "Black",
            "list_images" : [    
                "PictureForNike/Air-Max-07-Black.png",
                "PictureForNike/Air-Max-07-Black-2.png",
                "PictureForNike/Air-Max-07-Black-3.png",
                "PictureForNike/Air-Max-07-Black-4.png",
                "PictureForNike/Air-Max-07-Black-5.png",
                "PictureForNike/Air-Max-07-Black-6.png"]
        },{
            "name" : "Orange",
            "list_images" : [    
                "PictureForNike/Air-Max-07-Orange-1.png",
                "PictureForNike/Air-Max-07-Orange-2.png",
                "PictureForNike/Air-Max-07-Orange-3.png",
                "PictureForNike/Air-Max-07-Orange-4.png",
                "PictureForNike/Air-Max-07-Orange-5.png",
                "PictureForNike/Air-Max-07-Orange-6.png"]
        }
    ]
)
#Kids3
controller.add_product("Nike Lune Plus", 3500, "Kids",
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
    },[
        {
            "name" : "Neon",
            "list_images" :[    
                "PictureForNike/Lune-Plus.png",
                "PictureForNike/Lune-Plus-Neon-1.png",
                "PictureForNike/Lune-Plus-Neon-2.jfif",
                "PictureForNike/Lune-Plus-Neon-3.png",
                "PictureForNike/Lune-Plus-Neon-4.png",
                "PictureForNike/Lune-Plus-Neon-5.png",
                "PictureForNike/Lune-Plus-Neon-6.png"]
        }
        ,{
            "name" : "Azure",
            "list_images" : [    
                "PictureForNike/Lune-Plus-Azure.png",
                "PictureForNike/Lune-Plus-Azure-2.png",
                "PictureForNike/Lune-Plus-Azure-3.png",
                "PictureForNike/Lune-Plus-Azure-4.png",
                "PictureForNike/Lune-Plus-Azure-5.jfif",
                "PictureForNike/Lune-Plus-Azure-6.png"]
        },{
            "name" : "Black",
            "list_images" : [    
                "PictureForNike/Lune-Plus-Black-1.png",
                "PictureForNike/Lune-Plus-Black-2.png",
                "PictureForNike/Lune-Plus-Black-3.png",
                "PictureForNike/Lune-Plus-Black-4.png",
                "PictureForNike/Lune-Plus-Black-5.png",
                "PictureForNike/Lune-Plus-Black-6.jfif"]
        }
    ]
)
#Kids4
controller.add_product("Nike Air G Cut", 3900, "Kids",
    {
        "Orange": [50, "S"],
        "Orange": [50, "M"],
        "Orange": [50, "L"],
        "Pink": [80, "S"],
        "Pink": [80, "M"],
        "Pink": [80, "L"],
        "Black": [70, "S"],
        "Black": [70, "M"],
        "Black": [70, "L"],
    },[
        {
            "name" : "Orange",
            "list_images" : [    
                "PictureForNike/Air-G-Cut.png",
                "PictureForNike/Air-G-Cut-Orange-1.png",
                "PictureForNike/Air-G-Cut-Orange-2.png",
                "PictureForNike/Air-G-Cut-Orange-3.png",
                "PictureForNike/Air-G-Cut-Orange-4.png",
                "PictureForNike/Air-G-Cut-Orange-5.jfif",
                "PictureForNike/Air-G-Cut-Orange-6.png"]
        }
        ,{
            "name" : "Pink",
            "list_images" : [    
                "PictureForNike/Air-G-Cut-Pink.jfif",
                "PictureForNike/Air-G-Cut-Pink-2.png",
                "PictureForNike/Air-G-Cut-Pink-3.png",
                "PictureForNike/Air-G-Cut-Pink-4.png",
                "PictureForNike/Air-G-Cut-Pink-5.jfif",
                "PictureForNike/Air-G-Cut-Pink-6.jfif"]
        },{
            "name" : "Black",
            "list_images" :[    
                "PictureForNike/Air-G-Cut-Black-1.png",
                "PictureForNike/Air-G-Cut-Black-2.png",
                "PictureForNike/Air-G-Cut-Black-3.png",
                "PictureForNike/Air-G-Cut-Black-4.png",
                "PictureForNike/Air-G-Cut-Black-5.jfif",
                "PictureForNike/Air-G-Cut-Black-6.jfif"]
        }
    ]
)
#Kids5
controller.add_product("Nike Air Max 27'0", 4200, "Kids",
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
    },[
        {
            "name" : "Pink",
            "list_images" :[    
                "PictureForNike/Air-Max-27-0.png",
                "PictureForNike/Air-Max-27-0-Pink-1.png",
                "PictureForNike/Air-Max-27-0-Pink-2.png",
                "PictureForNike/Air-Max-27-0-Pink-3.png",
                "PictureForNike/Air-Max-27-0-Pink-4.png",
                "PictureForNike/Air-Max-27-0-Pink-5.png",
                "PictureForNike/Air-Max-27-0-Pink-6.png"]
        }
        ,{
            "name" : "Blue",
            "list_images" : [    
                "PictureForNike/Air-Max-27-0-Blue-1.png",
                "PictureForNike/Air-Max-27-0-Blue-2.png",
                "PictureForNike/Air-Max-27-0-Blue-3.png",
                "PictureForNike/Air-Max-27-0-Blue-4.png",
                "PictureForNike/Air-Max-27-0-Blue-5.png",
                "PictureForNike/Air-Max-27-0-Blue-6.png"]
        },{
            "name" : "Green",
            "list_images" : [    
                "PictureForNike/Air-Max-27-0-Green-1.png",
                "PictureForNike/Air-Max-27-0-Green-2.png",
                "PictureForNike/Air-Max-27-0-Green-3.png",
                "PictureForNike/Air-Max-27-0-Green-4.png",
                "PictureForNike/Air-Max-27-0-Green-5.jfif",
                "PictureForNike/Air-Max-27-0-Green-6.png"]
        }
    ]
)
#Kids6
controller.add_product("Nike Talunla'", 2900, "Kids",
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
    ,[
        {
            "name" : "Purple",
            "list_images" :[    
                "PictureForNike/Talunla.png",
                "PictureForNike/Talunla-Purple-1.png",
                "PictureForNike/Talunla-Purple-2.jfif",
                "PictureForNike/Talunla-Purple-3.png",
                "PictureForNike/Talunla-Purple-4.png",
                "PictureForNike/Talunla-Purple-5.jfif",
                "PictureForNike/Talunla-Purple-6.jfif"]
        }
        ,{
            "name" : "Galaxy",
            "list_images" : [    
                "PictureForNike/Talunla-Galaxy-1.png",
                "PictureForNike/Talunla-Galaxy-2.png",
                "PictureForNike/Talunla-Galaxy-3.png",
                "PictureForNike/Talunla-Galaxy-4.png",
                "PictureForNike/Talunla-Galaxy-5.png",
                "PictureForNike/Talunla-Galaxy-6.jfif"]
        },{
            "name" : "Black",
            "list_images" : [    
                "PictureForNike/Talunla-Black-1.png",
                "PictureForNike/Talunla-Black-2.png",
                "PictureForNike/Talunla-Black-3.png",
                "PictureForNike/Talunla-Black-4.png",
                "PictureForNike/Talunla-Black-5.jfif",
                "PictureForNike/Talunla-Black-6.jfif"]
        }
    ]
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
        "Blue": [100, "L"]
    },[
        {
            "name" : "White",
            "list_images" :[    
                "PictureForNike/Husky.png",
                "PictureForNike/Husky-White-1.png",
                "PictureForNike/Husky-White-2.jfif",
                "PictureForNike/Husky-White-3.png",
                "PictureForNike/Husky-White-4.png",
                "PictureForNike/Husky-White-5.png",
                "PictureForNike/Husky-White-6.png"]
        }
        ,{
            "name" : "Red",
            "list_images" : [    
                "PictureForNike/Husky-Red-1.png",
                "PictureForNike/Husky-Red-2.jfif",
                "PictureForNike/Husky-Red-3.png",
                "PictureForNike/Husky-Red-4.png",
                "PictureForNike/Husky-Red-5.jfif",
                "PictureForNike/Husky-Red-6.png"]
        },{
            "name" : "Blue",
            "list_images" : [    
                "PictureForNike/Husky-Blue-1.png",
                "PictureForNike/Husky-Blue-2.jfif",
                "PictureForNike/Husky-Blue-3.png",
                "PictureForNike/Husky-Blue-4.png",
                "PictureForNike/Husky-Blue-5.jfif",
                "PictureForNike/Husky-Blue-6.png"]
        }
    ]
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
        "Honey": [80, "L"]
    },[
        {
            "name" : "Black",
            "list_images" :[    
                "PictureForNike/Blast-77-7.png",
                "PictureForNike/Blast-77-7-Black-1.png",
                "PictureForNike/Blast-77-7-Black-2.png",
                "PictureForNike/Blast-77-7-Black-3.png",
                "PictureForNike/Blast-77-7-Black-4.png",
                "PictureForNike/Blast-77-7-Black-5.png",
                "PictureForNike/Blast-77-7-Black-6.png"]
        }
        ,{
            "name" : "White",
            "list_images" : [    
                "PictureForNike/Blast-77-7-White-1.png",
                "PictureForNike/Blast-77-7-White-2.png",
                "PictureForNike/Blast-77-7-White-3.png",
                "PictureForNike/Blast-77-7-White-4.png",
                "PictureForNike/Blast-77-7-White-5.png",
                "PictureForNike/Blast-77-7-White-6.png"]
        },{
            "name" : "Honey",
            "list_images" : [    
                "PictureForNike/Blast-77-7-Honey-.png",
                "PictureForNike/Blast-77-7-Honey-2.png",
                "PictureForNike/Blast-77-7-Honey-3.png",
                "PictureForNike/Blast-77-7-Honey-4.png",
                "PictureForNike/Blast-77-7-Honey-5.png",
                "PictureForNike/Blast-77-7-Honey-6.png"]
        }
    ]
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
        "Grey": [100, "L"]
    },[
        {
            "name" : "Blue",
            "list_images" :[    
                "PictureForNike/Fire-Plus.png",
                "PictureForNike/Fire-Plus-Blue-1.png",
                "PictureForNike/Fire-Plus-Blue-2.png",
                "PictureForNike/Fire-Plus-Blue-3.png",
                "PictureForNike/Fire-Plus-Blue-4.png",
                "PictureForNike/Fire-Plus-Blue-5.jfif",
                "PictureForNike/Fire-Plus-Blue-6.png"]
        }
        ,{
            "name" : "Colorful",
            "list_images" : [    
                "PictureForNike/Fire-Plus-Colorful-1.png",
                "PictureForNike/Fire-Plus-Colorful-2.png",
                "PictureForNike/Fire-Plus-Colorful-3.png",
                "PictureForNike/Fire-Plus-Colorful-4.png",
                "PictureForNike/Fire-Plus-Colorful-5.png",
                "PictureForNike/Fire-Plus-Colorful-6.png"]
        },{
            "name" : "Grey",
            "list_images" : [    
                "PictureForNike/Fire-Plus-Grey-.png",
                "PictureForNike/Fire-Plus-Grey-2.jfif",
                "PictureForNike/Fire-Plus-Grey-3.png",
                "PictureForNike/Fire-Plus-Grey-4.png",
                "PictureForNike/Fire-Plus-Grey-5.jfif",
                "PictureForNike/Fire-Plus-Grey-6.png"]
        }
    ]
)
#Kids10
controller.add_product("Nike Air Inmortel 00", 2500, "Kids",
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
    },[
        {
            "name" : "Orange",
            "list_images" :[    
                "PictureForNike/Air-Inmortel-00.png",
                "PictureForNike/Air-Inmortel-00-Orange-1.png",
                "PictureForNike/Air-Inmortel-00-Orange-2.png",
                "PictureForNike/Air-Inmortel-00-Orange-3.png",
                "PictureForNike/Air-Inmortel-00-Orange-4.png",
                "PictureForNike/Air-Inmortel-00-Orange-5.jfif",
                "PictureForNike/Air-Inmortel-00-Orange-6.png"]
        }
        ,{
            "name" : "White",
            "list_images" : [    
                "PictureForNike/Air-Inmortel-00-White-1.png",
                "PictureForNike/Air-Inmortel-00-White-2.png",
                "PictureForNike/Air-Inmortel-00-White-3.png",
                "PictureForNike/Air-Inmortel-00-White-4.png",
                "PictureForNike/Air-Inmortel-00-White-5.png",
                "PictureForNike/Air-Inmortel-00-White-6.png"]
        },{
            "name" : "Black",
            "list_images" : [    
                "PictureForNike/Air-Inmortel-00-Black-1.png",
                "PictureForNike/Air-Inmortel-00-Black-2.jfif",
                "PictureForNike/Air-Inmortel-00-Black-3.png",
                "PictureForNike/Air-Inmortel-00-Black-4.png",
                "PictureForNike/Air-Inmortel-00-Black-5.jfif",
                "PictureForNike/Air-Inmortel-00-Black-6.png"]
        }
    ]
)
#Kids11
controller.add_product("Nike Novel Dream SP", 2200, "Kids",
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
    },[
        {
            "name" : "Mint",
            "list_images" :[    
                "PictureForNike/Novel-Dream-SP.png",
                "PictureForNike/Novel-Dream-SP-Mint-1.png",
                "PictureForNike/Novel-Dream-SP-Mint-2.png",
                "PictureForNike/Novel-Dream-SP-Mint-3.png",
                "PictureForNike/Novel-Dream-SP-Mint-4.png",
                "PictureForNike/Novel-Dream-SP-Mint-5.png",
                "PictureForNike/Novel-Dream-SP-Mint-6.png"]
        }
        ,{
            "name" : "Red",
            "list_images" : [    
                "PictureForNike/Novel-Dream-SP-Red-1.png",
                "PictureForNike/Novel-Dream-SP-Red-2.png",
                "PictureForNike/Novel-Dream-SP-Red-3.png",
                "PictureForNike/Novel-Dream-SP-Red-4.png",
                "PictureForNike/Novel-Dream-SP-Red-5.jfif",
                "PictureForNike/Novel-Dream-SP-Red-6.png"]
        },{
            "name" : "White",
            "list_images" : [    
                "PictureForNike/Novel-Dream-SP-White-1.png",
                "PictureForNike/Novel-Dream-SP-White-2.png",
                "PictureForNike/Novel-Dream-SP-White-3.png",
                "PictureForNike/Novel-Dream-SP-White-4.png",
                "PictureForNike/Novel-Dream-SP-White-5.png",
                "PictureForNike/Novel-Dream-SP-White-6.png"]
        }
    ]
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
    },[
        {
            "name" : "Brown",
            "list_images" :[    
                "PictureForNike/Tataui-03.png",
                "PictureForNike/Tataui-03-Brown-1.jfif",
                "PictureForNike/Tataui-03-Brown-2.png",
                "PictureForNike/Tataui-03-Brown-3.jfif",
                "PictureForNike/Tataui-03-Brown-4.png",
                "PictureForNike/Tataui-03-Brown-5.jfif",
                "PictureForNike/Tataui-03-Brown-6.png"]
        }
        ,{
            "name" : "Colorful",
            "list_images" : [    
                "PictureForNike/Tataui-03-Colorful-1.png",
                "PictureForNike/Tataui-03-Colorful-2.png",
                "PictureForNike/Tataui-03-Colorful-3.jfif",
                "PictureForNike/Tataui-03-Colorful-4.png",
                "PictureForNike/Tataui-03-Colorful-5.png",
                "PictureForNike/Tataui-03-Colorful-6.png"]
        },{
            "name" : "Grey",
            "list_images" : [    
                "PictureForNike/Tataui-03-Grey-1.png",
                "PictureForNike/Tataui-03-Grey-2.png",
                "PictureForNike/Tataui-03-Grey-3.jfif",
                "PictureForNike/Tataui-03-Grey-4.png",
                "PictureForNike/Tataui-03-Grey-5.jfif",
                "PictureForNike/Tataui-03-Grey-6.jfif"]
        }
    ]
)


class ProductIn(BaseModel):
    name: str
    price: int
    gender: str
    style : dict


    

@router.get("/product/all", tags =["Product"]) 
def get_product_detail():
    return controller.get_all_product()


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