from fastapi import FastAPI
from pydantic import BaseModel

from camosam_backend.controllers.gift_list_controller import add_gift

class Gift(BaseModel):
    name: str
    image_url: str
    price: float
    is_active: bool


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/gift")
def store_gift(gift: Gift) -> tuple:
    return add_gift(gift)