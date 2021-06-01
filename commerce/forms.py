from django import forms
from django.forms import ModelForm
from .models import Product, Order
from django.core.exceptions import ValidationError

class ProductForm(ModelForm):
    """Register products from Product Models"""
    class Meta:
        model = Product
        fields = "__all__"

class OrderForm(ModelForm):
    """Register products ordem from Order Models"""
    class Meta:
        model = Order
        fields = ['product_name', 'suggested_price', 'amount']

    