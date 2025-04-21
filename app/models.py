from pydantic import BaseModel, Field, constr
from typing import List

class Item(BaseModel):
    shortDescription: constr(pattern=r"^[\w\s\-]+$")
    price: constr(pattern=r"^\d+\.\d{2}$")

class Receipt(BaseModel):
    retailer: constr(pattern=r"^[\w\s\-\&]+$")
    purchaseDate: constr(pattern=r"^\d{4}-\d{2}-\d{2}$")
    purchaseTime: constr(pattern=r"^\d{2}:\d{2}$")
    items: List[Item]
    total: constr(pattern=r"^\d+\.\d{2}$")
