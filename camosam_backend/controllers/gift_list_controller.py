from ..services.gift_list_service import (
    store_gift,
    show_gifts_list,
    update_gift,
    delete_gift
)


def add_gift(gift: dict) -> dict:
    try:
        result, error = store_gift(**gift)
        if error:
            return {'[ERROR] Cannot save gift': str(error)}
        return result
    except Exception as error:
        return {'[ERROR] Cannot save gift': f'Invalid data: {error}'}

def gifts_list() -> list | dict:
    try:
        gifts_list, error = show_gifts_list()
        if error:
            return {'[ERROR] Cannot show gifts list': str(error)}
        return gifts_list
    except Exception as error:
        return {'[ERROR] Cannot show gifts list': f'Invalid data: {error}'}

def restore_gift(gift_id: int, data: dict) -> list | dict:
    try:
        formated_data = {
            key: value
            for key, value in data.items()
            if value is not None and value != ''
        }
        updated_gift, error = update_gift(gift_id, formated_data)
        if error:
            return {'[ERROR] Cannot update gift': str(error)}
        return updated_gift
    except Exception as error:
        return {'[ERROR] Cannot update gift': f'Invalid data: {error}'}

def delete_gift_instance(gift_id: int) -> dict:
    try:
        _, error = delete_gift(gift_id)
        if error:
            return {'error': str(error)}
        return {'message': f'Record deleted'}
    except Exception as e:
        return {'error': f'Invalid data: {e}'}