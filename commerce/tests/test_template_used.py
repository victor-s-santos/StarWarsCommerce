import pytest
from django.shortcuts import resolve_url as url

path_list_authenticated_templates = [
    ('commerce:product_list', 'commerce/product_list.html'),
    ('commerce:order_list', 'commerce/order_list.html'),
    ('commerce:register_order', 'commerce/register_order.html'),
]

path_list_superuser_templates = [
    ('commerce:product_register', 'commerce/product_register.html'),   
]

#authenticated user
@pytest.mark.parametrize('name, template_name', path_list_authenticated_templates)
def test_template_to_authenticated_user(client_with_user, name, template_name):
    """Must return the corresponding page for unauthenticated user"""
    response = client_with_user.get(url(name)) 
    assert template_name in (template.name for template in response.templates)

#admin user
@pytest.mark.parametrize('name, template_name', path_list_authenticated_templates)
def test_template_to_admin_user(admin_client, name, template_name):
    """Must return the corresponding page for unauthenticated user"""
    response = admin_client.get(url(name)) 
    assert template_name in (template.name for template in response.templates)