from fastapi import FastAPI

from camosam_backend.models.validation_models import (
    StoredGift,
    UpdatedGift,
    StoredGuest,
    UpdatedGuest
)
from camosam_backend.controllers.gift_list_controller import (
    add_gift,
    gifts_list,
    restore_gift,
    delete_gift_instance,
)
from camosam_backend.controllers.guest_list_controller import (
    add_guest,
    guests_list,
    restore_guest,
    delete_guest_instance,
)


app = FastAPI()


@app.get('/liveness')
def read_root():
    return {'msg': 'CAMOSAM OK'}

@app.post('/gift')
def store_gift(gift: StoredGift) -> dict:
    return add_gift(dict(gift))

@app.get('/gift')
def show_gift() -> list | dict:
    return gifts_list()

@app.patch('/gift/{gift_id}')
def update_gift(gift_id: int, gift: UpdatedGift) -> dict:
    return restore_gift(gift_id, dict(gift))

@app.delete('/gift/{gift_id}')
def delete_gift(gift_id: int) -> dict:
    return delete_gift_instance(gift_id)

@app.post('/guest')
def store_guest(guest: StoredGuest) -> dict:
    return add_guest(dict(guest))

@app.get('/guest')
def show_guest() -> list | dict:
    return guests_list()

@app.patch('/guest/{guest_id}')
def update_guest(guest_id: int, guest: UpdatedGuest) -> dict:
    return restore_guest(guest_id, dict(guest))

@app.delete('/guest/{guest_id}')
def delete_guest(guest_id: int) -> dict:
    return delete_guest_instance(guest_id)