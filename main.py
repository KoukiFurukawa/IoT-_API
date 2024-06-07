from fastapi import FastAPI
from firebase_config.db_conf import GetAllDoc
from pydantic import BaseModel
import firebase_admin
from firebase_admin import firestore
    
class parkingData(BaseModel):
    deviceId: str
    percent : float

app = FastAPI()

GetAllDoc("Users")

@app.get("/")
def read_root():
    keep_db
    return {"Hello": "World"}

@app.post("/")
def receive_parking_data(pk_data: parkingData):
    state = {
        "state" : "ok"
    }
    keep_db()
    return state


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/degree")
def read_degree():
    return







def keep_db(pk_data: parkingData):
    app = firebase_admin.initialize_app()
    db = firestore.client()
    deviceId = pk_data.deviceId

    data = {"item_id": 30, "percent": 70}
    db.collection("Parking").document(deviceId).set(data)













