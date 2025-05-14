from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import redis


app = FastAPI()
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

class Item(BaseModel):
    key: str
    value: str

class KeysRequest(BaseModel):
    keys: List[str]

class ItemsRequest(BaseModel):
    items: List[Dict[str, str]]

@app.get("/all")
def get_all_items():
    all_items = {}
    for key in r.scan_iter():
        value = r.get(key)
        all_items[key] = value
    return all_items

@app.post("/set")
def set_item(item: Item):
    r.set(item.key, item.value)
    return {"message": "success"}

@app.get("/get/{key}")
def get_item(key: str):
    value = r.get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"key": key, "value": value}

@app.post("/mget")
def mget_items(keys_request: KeysRequest):
    values = r.mget(keys_request.keys)
    return dict(zip(keys_request.keys, values))

@app.post("/mset")
def mset_items(items_request: ItemsRequest):
    for item in items_request.items:
        r.set(item['key'], item['value'])
    return {"message": "success"}

@app.post("/mdelete")
def mdelete_items(keys_request: KeysRequest):
    r.delete(*keys_request.keys)
    return {"message": "success"}