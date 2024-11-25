from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    price: float
    is_available: bool