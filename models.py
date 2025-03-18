from datetime import datetime
from pydantic import BaseModel, Field

class ItemModel(BaseModel):
    id: int
    name: str
    price: float
    date_updated: datetime = Field(default_factory=datetime.now)

class PriceUpdateModel(BaseModel):
    price: float
    date_updated: datetime = Field(default_factory=datetime.now)
