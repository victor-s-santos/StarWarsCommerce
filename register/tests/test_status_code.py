import pytest
from django.shortcuts import resolve_url as url

path_list_status_code_302 = [
    ('profile'),
    ('logout'),
]

path_list_status_code_200 = [
    ('login'),
    ('profile'),
    ('reset_password'),
    ('password_reset_done'),
    ('password_reset_complete'),
]

#unauthenticated user 
@pytest.mark.parametrize('name', path_list_status_code_302)
def test_status_code_302(client, name):
    """Must return status code 302"""
    assert client.get(url(name)).status_code == 302

#authenticated user
@pytest.mark.parametrize('name', path_list_status_code_200)
def test_status_code_200(client_with_user, name):
    """Must return status code 200"""
    assert client_with_user.get(url(name)).status_code == 200