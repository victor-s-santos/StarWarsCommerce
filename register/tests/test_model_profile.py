import pytest
from pytest import raises
from model_mommy import mommy
from register.models import Profile

@pytest.mark.django_db
def test_publish_profile():
    """Must register objects in model Profile"""
    assert Profile.objects.count() == 0
    mommy.make(Profile)
    assert Profile.objects.count() == 1
    mommy.make(Profile)
    assert Profile.objects.count() == 2

@pytest.mark.django_db
def test_fields_profile():
    """Must return true for any field"""
    assert Profile.user
    assert Profile.home_planet
    assert Profile.height
    assert Profile.mass

@pytest.mark.django_db
def test_invalid_fields_profile():
    """Must return attributeerror for any field"""
    with raises(AttributeError):
        Profile.usuario
    with raises(AttributeError):
        Profile.planeta_natal
    with raises(AttributeError):
        Profile.altura
    with raises(AttributeError):
        Profile.massa