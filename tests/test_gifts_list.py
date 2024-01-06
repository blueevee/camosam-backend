from ..camosam_backend.controllers.gift_list_controller import add_gift

def test_should_not_add_gift_without_image():
    gift = {
        'name':'g',
        'price': 12.30,
        'active': True
    }
    assert add_gift(gift) == {
            'error': 'Incomplete model, missing fields: image_url'
            }, 422