from ..models.guests_model import Guest


def store_guest(name: str, email: str, phone: str) -> (dict, None):
    try:

        stored_guest = Guest.create(
            name=name,
            email=email,
            phone=phone,
        )

        return stored_guest.__data__, None
    except Exception as error:
        return None, error

def show_guest_list() -> (dict, None):
    try:
        guest_list = list(Guest.select().dicts())
        return guest_list, None
    except Exception as error:
        return None, error

def update_guest(guest_id: int, data: dict) -> (dict, None):
    try:
        query = Guest.update(**data).where( Guest.id == guest_id )
        query.execute()
        updated_guest = Guest.get_or_none(Guest.id == guest_id)
        if updated_guest:
            result = updated_guest.__dict__['__data__']
            return result, None
        return None, 'Registro não encontrado'
    except Exception as error:
        return None, error

def delete_guest(guest_id: int) -> (bool, None):
    try:
        guest_select = Guest.get_or_none(Guest.id == guest_id)
        if guest_select:
            guest_select.delete_instance()
        return True, None
    except Exception as error:
        return None, error