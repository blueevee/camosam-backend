from ..services.guest_list_service import (
    store_guest,
    show_guest_list,
    update_guest,
    delete_guest
)


def add_guest(guest: dict) -> dict:
    try:
        result, error = store_guest(**guest)
        if error:
            return {'[ERROR] Cannot save guest': str(error)}
        return result
    except Exception as error:
        return {'[ERROR] Cannot save guest': f'Invalid data: {error}'}

def guests_list() -> list | dict:
    try:
        guests_list, error = show_guest_list()
        if error:
            return {'[ERROR] Cannot show guests list': str(error)}
        return guests_list
    except Exception as error:
        return {'[ERROR] Cannot show guests list': f'Invalid data: {error}'}

def restore_guest(guest_id: int, data: dict) -> list | dict:
    try:
        formated_data = {
            key: value
            for key, value in data.items()
            if value is not None and value != ''
        }
        updated_guest, error = update_guest(guest_id, formated_data)
        if error:
            return {'[ERROR] Cannot update guest': str(error)}
        return updated_guest
    except Exception as error:
        return {'[ERROR] Cannot update guest': f'Invalid data: {error}'}

def delete_guest_instance(guest_id: int) -> dict:
    try:
        _, error = delete_guest(guest_id)
        if error:
            return {'error': str(error)}
        return {'message': f'Record deleted'}
    except Exception as e:
        return {'error': f'Invalid data: {e}'}