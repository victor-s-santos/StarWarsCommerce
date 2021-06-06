from django.shortcuts import resolve_url as url
import pytest

list_reverse_names_authenticated = [
    ('commerce:product_list', 200),
    ('commerce:order_list', 200),
    ('commerce:register_order', 200),
    ('commerce:product_register', 302),
]

list_reverse_names_admin = [
    ('commerce:product_list', 200),
    ('commerce:order_list', 200),
    ('commerce:register_order', 200),
    ('commerce:product_register', 200),
    ('commerce:register_order', 200),
]



@pytest.mark.parametrize('path, status_code', list_reverse_names_authenticated)
def test_render_views(client_with_user, path, status_code):
    assert client_with_user.get(url(path)).status_code == status_code

@pytest.mark.parametrize('path, status_code', list_reverse_names_admin)
def test_render_views_admin(admin_client, path, status_code):
    assert admin_client.get(url(path)).status_code == status_code






    