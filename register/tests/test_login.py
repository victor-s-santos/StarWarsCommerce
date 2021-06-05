import pytest
from django.contrib.auth import login, authenticate

@pytest.mark.django_db
def test_user_login_success(django_user_model):
    """Must return authenticated user"""
    user = django_user_model.objects.create_user(password='senha_secreta', username='preciso_usar_base_model', email='test@email.com')
    user = authenticate(username='test@email.com', password='senha_secreta')
    assert (user is not None)
    assert (user.is_authenticated == True)

@pytest.mark.django_db
def test_user_login_fail_email(django_user_model):
    """Must return True to user is None"""
    user = django_user_model.objects.create_user(password='senha_secreta', username='preciso_usar_base_model', email='test@email.com')
    user = authenticate(username='test232@email.com', password='senha_secreta')
    assert (user is None)

@pytest.mark.django_db
def test_user_login_fail_password(django_user_model):
    """Must return user None"""
    user = django_user_model.objects.create_user(password='senha_secreta', username='preciso_usar_base_model', email='test@email.com')
    user = authenticate(username='test@email.com', password='senha_discreta')
    assert (user is None)