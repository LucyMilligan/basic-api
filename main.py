from fastapi import FastAPI, HTTPException
import uvicorn

from models import ItemModel, PriceUpdateModel

app = FastAPI()


food_prices = [
    {"id": 1, "name": "apples", "price": 1.40, "date_updated": "2025-03-18T19:00:00.000"},
    {"id": 2, "name": "bananas", "price": 0.90, "date_updated": "2025-03-18T19:00:00.000"},
    {"id": 3, "name": "avacados", "price": 2.50, "date_updated": "2025-03-18T19:00:00.000"},
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items")
async def get_items(skip: int = 0, limit: int = 2):
    """endpoint to get a paginated list of items.

    :param skip: number of items to skip
    :param limit: number of items to return
    """
    return food_prices[skip:skip+limit]

@app.get("/items/{item_id}")
async def get_item_by_id(item_id: str):
    for item in food_prices:
        if item["id"] == int(item_id):
            return item

    raise HTTPException(
        status_code=404,
        detail="no such item exists"
    )

@app.post("/items")
async def create_item(item: ItemModel):
    food_prices.append(item)
    return item

@app.patch("/items/{item_id}")
async def update_item_price(item_id: str, price_model: PriceUpdateModel):
    for item in food_prices:
        if item["id"] == int(item_id):
            item["price"] = price_model.price
            item["date_updated"] = price_model.date_updated
            return item

if __name__ == "__main__":
    uvicorn.run(app)