from ..services.gift_list_service import store_gift


def add_gift(gift: dict) -> tuple:
    try:
        required_fields = ['name', 'image_url','price']
        if all(gift.get(field) for field in required_fields):
            result, error = store_gift(**gift)
            if error:
                return {'[ERROR] Cannot save gift': str(error)}, 500
            return result, 201

        missing_fields = [
            field for field in required_fields if not gift.get(field)
        ]
        return {
            'error': f'Incomplete model, missing fields: {", ".join(missing_fields)}'
        }, 422
    except Exception as error:
        return {'[ERROR] Cannot save gift': f'Invalid data: {error}'}, 400