import pytest
from django.shortcuts import resolve_url as url
from commerce.forms import ProductForm, OrderForm

def test_form_product(client_with_user):
    """Context must have ProductForm"""
    form = client_with_user.get(url('commerce:product_register')).context['form']
    assert isinstance(form, ProductForm)