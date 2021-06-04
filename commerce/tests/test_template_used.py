import pytest
from django.urls import reverse

path_list_authenticated_templates = [
    ('product_list', 'commerce/product_list.html'),
    ('order_list', 'commerce/order_list.html'),
    ('register_order', 'commerce/register_order.html'),
]

path_list_superuser_templates = [
    ('product_register', 'commerce/product_register.html'),
    
]

#authenticated user
@pytest.mark.parametrize('link, template_name', path_list_authenticated_templates)
def test_template_to_authenticated_user(client_with_user, link, template_name):
    """Must return the corresponding page for unauthenticated user"""
    response = client_with_user.get(reverse(link)) 
    assert template_name in (template.name for template in response.templates)

#admin user
@pytest.mark.parametrize('link, template_name', path_list_authenticated_templates)
def test_template_to_admin_user(admin_client, link, template_name):
    """Must return the corresponding page for unauthenticated user"""
    response = admin_client.get(reverse(link)) 
    assert template_name in (template.name for template in response.templates)