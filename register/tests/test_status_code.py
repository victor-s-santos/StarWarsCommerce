import pytest
import requests

path_list_status_code_302 = [
    ('/register/infos/'),
    ('/logout/'),
]

path_list_status_code_200 = [
    ('/register/infos/'),
    ('/register/reset_password/'),
    ('/register/reset_password_sent/'),
    ('/register/reset_password_complete/'),
]

#unauthenticated user 
@pytest.mark.parametrize('link', path_list_status_code_302)
def test_status_code_302(client, link):
    """Must return status code 302"""
    assert client.get(link).status_code == 302

#authenticated user
@pytest.mark.parametrize('link', path_list_status_code_200)
def test_status_code_200(client_with_user, link):
    """Must return status code 200"""
    assert client_with_user.get(link).status_code == 200