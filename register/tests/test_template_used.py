import pytest
from django.shortcuts import resolve_url as url

path_name_unauthenticated_templates = [
    ('login', 'registration/login.html'),
    ('register', 'register/register.html'),
    ('reset_password', 'password_reset/password_reset.html'),
    ('password_reset_done', 'password_reset/password_reset_sent.html'),
    ('password_reset_complete', 'password_reset/password_reset_complete.html')
]

path_list_authenticated_templates = [
    ('profile', 'register/infos.html'),
]

#unauthenticated user
@pytest.mark.parametrize('name, template_name', path_name_unauthenticated_templates)
def test_template_to_unauthenticated_user(client, name, template_name):
    """Must return the corresponding page for unauthenticated user"""
    response = client.get(url(name)) 
    assert template_name in (template.name for template in response.templates)