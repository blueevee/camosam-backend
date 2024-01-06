from ..models.gifts_model import Gifts


def store_gift(name: str, price: float, image_url: str, is_active: bool = True ) -> (dict, None):
    try:

        stored_gift = Gifts.create(
            name=name,
            image_url=image_url,
            price=price,
            is_active=is_active,
        )

        return stored_gift.__data__, None
    except Exception as error:
        return None, error