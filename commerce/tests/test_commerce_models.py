import pytest
from pytest import raises
from model_mommy import mommy
from commerce.models import Product, Order
from django.db.models import CharField, FloatField, IntegerField, OneToOneField, ForeignKey

list_product_fields = [
    (Product._meta.get_field("product_name"), CharField),
    (Product._meta.get_field("unit_price"), FloatField),
    (Product._meta.get_field("multiple"), IntegerField),
]

list_order_fields = [
    (Order._meta.get_field("user"), OneToOneField),
    (Order._meta.get_field("product_name"), ForeignKey),
    (Order._meta.get_field("suggested_price"), FloatField),
    (Order._meta.get_field("amount"), IntegerField),

]

@pytest.mark.django_db
def test_register_product():
    """Must register objects in model Product"""
    assert Product.objects.count() == 0
    mommy.make(Product)
    assert Product.objects.count() == 1
    mommy.make(Product)
    assert Product.objects.count() == 2

@pytest.mark.django_db
def test_register_order():
    """Must register objects in model Order"""
    assert Order.objects.count() == 0
    mommy.make(Order)
    assert Order.objects.count() == 1
    mommy.make(Order)
    assert Order.objects.count() == 2

@pytest.mark.django_db
def test_exists_fields_product():
    """Must return true for any field"""
    assert Product.product_name
    assert Product.unit_price
    assert Product.multiple

@pytest.mark.django_db
def test_exists_fields_order():
    """Must return true for any field"""
    assert Order.user
    assert Order.product_name
    assert Order.suggested_price
    assert Order.amount

@pytest.mark.django_db
@pytest.mark.parametrize('product_field, db_field', list_product_fields)
def test_product_fields(product_field, db_field):
    """Must return the specific django models field"""
    p = product_field
    f = db_field
    assert type(p) == f

@pytest.mark.django_db
@pytest.mark.parametrize('order_field, db_field', list_order_fields)
def test_order_fields(order_field, db_field):
    """Must return the specific django models field"""
    o = order_field
    f = db_field
    assert type(o) == f

@pytest.mark.django_db
def test_invalid_fields_product():
    """Must return attributeerror for any field"""
    with raises(AttributeError):
        Product.nome_produto
    with raises(AttributeError):
        Product.preco_unitario
    with raises(AttributeError):
        Product.multiplo

@pytest.mark.django_db
def test_invalid_fields_order():
    """Must return attributeerror for any field"""
    with raises(AttributeError):
        Order.usuario
    with raises(AttributeError):
        Order.nome_produto
    with raises(AttributeError):
        Order.preco_sugerido
    with raises(AttributeError):
        Order.quantidade