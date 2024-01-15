from pydantic import BaseModel


class StoredGift(BaseModel):
    name: str
    image_url: str
    price: float
    is_active: bool = True

class UpdatedGift(BaseModel):
    name: str = None
    image_url: str = None
    price: float = None
    is_active: bool = None

class StoredGuest(BaseModel):
    name: str
    email: str
    phone: str

class UpdatedGuest(BaseModel):
    name: str = None
    email: str = None
    phone: str = None