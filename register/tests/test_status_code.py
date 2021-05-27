import pytest
import requests

path_list_status_code_302 = [
    ('/register/infos/')
]

#unauthenticated user 
@pytest.mark.parametrize('link', path_list_status_code_302)
def test_status_code_302(client, link):
    """Must return status code 302"""
    assert client.get(link).status_code == 302

#authenticated user
@pytest.mark.parametrize('link', path_list_status_code_302)
def test_status_code_200(client_with_user, link):
    """Must return status code 200"""
    assert client_with_user.get(link).status_code == 200