import pytest

path_list_unauthenticated_templates = [
    ('/login/', 'registration/login.html'),
    ('/register/', 'register/register.html'),
    ('/register/reset_password/', 'password_reset/password_reset.html'),
    ('/register/reset_password_sent/', 'password_reset/password_reset_sent.html'),
    ('/register/reset/<uidb64>/<token>/', 'password_reset_confirm.html'),
    ('/register/reset_password_complete/', 'password_reset/password_reset_complete.html')
]

path_list_authenticated_templates = [
    ('/register/infos/', 'register/infos.html'),
]

#unauthenticated user
@pytest.mark.parametrize('link, template_name', path_list_unauthenticated_templates)
def test_template_to_unauthenticated_user(client, link, template_name):
    """Must return the corresponding page for unauthenticated user"""
    response = client.get(link) 
    assert template_name in (template.name for template in response.templates)