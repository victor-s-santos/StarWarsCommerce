from django.urls import reverse
import pytest

list_reverse_names_authenticated = [
    ('product_list', 200),
    ('order_list', 200),
    ('register_order', 200),
    ('product_register', 302),
]

list_reverse_names_admin = [
    ('product_list', 200),
    ('order_list', 200),
    ('register_order', 200),
    ('product_register', 200),
    ('register_order', 200),
]



@pytest.mark.parametrize('path, status_code', list_reverse_names_authenticated)
def test_render_views(client_with_user, path, status_code):
    assert client_with_user.get(reverse(path)).status_code == status_code

@pytest.mark.parametrize('path, status_code', list_reverse_names_admin)
def test_render_views_admin(admin_client, path, status_code):
    assert admin_client.get(reverse(path)).status_code == status_code






    