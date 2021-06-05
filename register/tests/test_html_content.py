import pytest
from django.shortcuts import resolve_url as url

path_list_must_have_csrf_token = [
    ('login'),
    ('register'),
    ('profile'),
    ('reset_password'),
]

path_form_tags_list = [
    ('login', '<form'),
    ('register', '<form'),
    ('profile', '<form'),
    ('reset_password', '<form'),
]

path_input_list = [
    ('login', '<input', 4),
    ('register', '<input', 8),
    ('profile', '<input', 5),
    ('reset_password', '<input', 3),
]

@pytest.mark.parametrize('name', path_list_must_have_csrf_token)
def test_csrf_token(client_with_user, name):
    """Must contain csrf_token"""
    response = client_with_user.get(url(name))
    assert 'csrfmiddlewaretoken' in str(response.content)

@pytest.mark.parametrize('name, formtags', path_form_tags_list)
def test_form_tags(client_with_user, name, formtags):
    """Must contain one form_tag"""
    response = client_with_user.get(url(name))
    count_form = str(response.content).count(formtags)
    assert count_form == 1

@pytest.mark.parametrize('name, html_input, number', path_input_list)
def test_input_number(client_with_user, name, html_input, number):
    """Must contain certain number of inputs"""
    response = client_with_user.get(url(name))
    count_input = str(response.content).count(html_input)
    assert count_input == number