import pytest
from pytest import raises
from model_mommy import mommy
from register.models import Profile
from django.db.models import CharField, FloatField, OneToOneField, ForeignKey

list_profile_fields = [
    (Profile._meta.get_field("user"), OneToOneField),
    (Profile._meta.get_field("home_planet"), CharField),
    (Profile._meta.get_field("height"), FloatField),
    (Profile._meta.get_field("mass"), FloatField)
]

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

@pytest.mark.django_db
@pytest.mark.parametrize('profile_field, db_field', list_profile_fields)
def test_profile_fields(profile_field, db_field):
    """Must return the specific django models field"""
    p = profile_field
    f = db_field
    assert type(p) == f