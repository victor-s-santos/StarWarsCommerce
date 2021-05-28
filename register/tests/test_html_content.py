import pytest

path_list_must_have_csrf_token = [
    ('/login/'),
    ('/register/'),
    ('/register/infos/'),
    ('/register/reset_password/'),
]

path_form_tags_list = [
    ('/login/', '<form'),
    ('/register/', '<form'),
    ('/register/infos/', '<form'),
    ('/register/reset_password/', '<form'),
]

path_input_list = [
    ('/login/', '<input', 4),
    ('/register/', '<input', 8),
    ('/register/infos/', '<input', 5),
    ('/register/reset_password/', '<input', 3),
]

@pytest.mark.parametrize('link', path_list_must_have_csrf_token)
def test_csrf_token(client_with_user, link):
    """Must contain csrf_token"""
    response = client_with_user.get(link)
    assert 'csrfmiddlewaretoken' in str(response.content)

@pytest.mark.parametrize('link, formtags', path_form_tags_list)
def test_form_tags(client_with_user, link, formtags):
    """Must contain one form_tag"""
    response = client_with_user.get(link)
    count_form = str(response.content).count(formtags)
    assert count_form == 1

@pytest.mark.parametrize('link, html_input, number', path_input_list)
def test_input_number(client_with_user, link, html_input, number):
    """Must contain certain number of inputs"""
    response = client_with_user.get(link)
    count_input = str(response.content).count(html_input)
    assert count_input == number