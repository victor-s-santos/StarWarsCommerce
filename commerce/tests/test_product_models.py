import pytest
from pytest import raises
from model_mommy import mommy
from commerce.models import Product

@pytest.mark.django_db
def test_register_product():
    """Must register objects in model Product"""
    assert Product.objects.count() == 0
    mommy.make(Product)
    assert Product.objects.count() == 1
    mommy.make(Product)
    assert Product.objects.count() == 2

@pytest.mark.django_db
def test_fields_profile():
    """Must return true for any field"""
    assert Product.product_name
    assert Product.unit_price
    assert Product.multiple

@pytest.mark.django_db
def test_invalid_fields_profile():
    """Must return attributeerror for any field"""
    with raises(AttributeError):
        Product.nome_produto
    with raises(AttributeError):
        Product.preco_unitario
    with raises(AttributeError):
        Product.multiplo