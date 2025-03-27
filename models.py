from typing import List, Optional, Union
from pydantic import BaseModel, Field

class Price(BaseModel):
    price: float = Field(description="The price of the item")
    serving: Optional[Union[str, int, float]] = Field(None, description="The serving size or type")

class MenuItem(BaseModel):
    item_name: str = Field(description="The name of the menu item")
    ingredients: List[str] = Field(description="List of ingredients used in the item")
    prices: List[Price] = Field(description="List of price options for the item")
    section_course: str = Field(description="The section or course of the menu item")

class DataPoints(BaseModel):
    restaurant_name: str = Field(description="The name of the restaurant of {entity_name}")
    location: str = Field(description="The location of the {entity_name}")
    contact: str = Field(description="The contact information of the restaurant {entity_name}")
    opening_hours: str = Field(description="The opening hours of the restaurant {entity_name}")
    menus: List[MenuItem] = Field(description="The menu of the restaurant {entity_name}, do NOT make things up, only provide information that you found; leave empty array if you cant find any;")