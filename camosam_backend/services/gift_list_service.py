from ..models.gifts_model import Gift


def store_gift(name: str, price: float, image_url: str, is_active: bool = True ) -> (dict, None):
    try:

        stored_gift = Gift.create(
            name=name,
            image_url=image_url,
            price=price,
            is_active=is_active,
        )

        return stored_gift.__data__, None
    except Exception as error:
        return None, error

def show_gifts_list() -> (dict, None):
    try:
        gifts_list = list(Gift.select().dicts())
        return gifts_list, None
    except Exception as error:
        return None, error

def update_gift(gift_id: int, data: dict) -> (dict, None):
    try:
        query = Gift.update(**data).where( Gift.id == gift_id )
        query.execute()
        updated_gift = Gift.get_or_none(Gift.id == gift_id)
        if updated_gift:
            result = updated_gift.__dict__['__data__']
            return result, None
        return None, 'Registro não encontrado'
    except Exception as error:
        return None, error

def delete_gift(gift_id: int) -> (bool, None):
    try:

        gift_to_delete = Gift.get_or_none(Gift.id == gift_id)
        if gift_to_delete:
            gift_to_delete.delete_instance()
        return True, None
    except Exception as error:
        return None, error