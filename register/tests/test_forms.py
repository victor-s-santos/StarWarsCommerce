import pytest
from django.shortcuts import resolve_url as url
from register.forms import RegisterForm, ProfileForm

#RegisterForm
def test_form_signup(client):
    """Context must have RegisterForm"""
    form = client.get(url('register:register')).context['form']
    assert isinstance(form, RegisterForm)

def test_form_number_of_fields(client):
    """Form must have 6 fields"""
    form = client.get(url('register:register')).context['form']
    assert len(list(form.fields)) == 6

def test_signup_form_fields(client):
    """Form must have these specific fields"""
    form = client.get(url('register:register')).context['form']
    specific_fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']
    assert len(specific_fields) == len(list(form.fields))
    difference = [x for x in specific_fields + list(form.fields) if x not in specific_fields or x not in list(form.fields)]
    assert len(difference) == 0

#ProfileForm
def test_form_signup_infos(client_with_user):
    """Context must have ProfileForm"""
    form = client_with_user.get(url('register:profile')).context['form']
    assert isinstance(form, ProfileForm)

def test_form_number_of_fields_profileform(client_with_user):
    """Form must have 3 fields"""
    form = client_with_user.get(url('register:profile')).context['form']
    assert len(list(form.fields)) == 3

def test_signup_infos_form_fields(client_with_user):
    """Form must have these specific fields"""
    form = client_with_user.get(url('register:profile')).context['form']
    specific_fields = ['home_planet', 'height', 'mass']
    assert len(specific_fields) == len(list(form.fields))
    difference = [x for x in specific_fields + list(form.fields) if x not in specific_fields or x not in list(form.fields)]
    assert len(difference) == 0