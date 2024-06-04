from fastapi import FastAPI
from firebase_config.db_conf import GetAllDoc
from pydantic import BaseModel


class Item(BaseModel):
    deviceId: str
    degree  : float
    price: float
    tax: float | None = None

app = FastAPI()

GetAllDoc("Users")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/degree")
def read_degree():
    return