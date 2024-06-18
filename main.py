from fastapi import FastAPI
from firebase_config.db_conf import GetAllDoc, insertParkingData
from pydantic import BaseModel
    
class parkingData(BaseModel):
    parkingId: str
    percent : float

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/")
def receive_parking_data(pk_data: parkingData):
    state = {
        "state" : "ok"
    }
    insertParkingData(pk_data)
    return state


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/degree")
def read_degree():
    return
