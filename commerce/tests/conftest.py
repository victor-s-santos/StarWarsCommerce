import pytest
from model_mommy import mommy
from commerce.models import Product

@pytest.fixture
def logged_user(django_user_model):
    """Create user with model mommy"""
    logged_user = mommy.make(django_user_model)
    logged_user.email = logged_user.email.lower()
    logged_user.save()
    return logged_user

@pytest.fixture
def client_with_user(client, django_user_model, logged_user):
    """Force user login"""
    client.force_login(logged_user)
    return client
