from fastapi import FastAPI
from firebase_config.db_conf import GetAllDoc

app = FastAPI()

GetAllDoc("Users")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
