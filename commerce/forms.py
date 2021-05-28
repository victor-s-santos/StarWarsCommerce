from django import forms
from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    """Register products from Product Models"""
    class Meta:
        model = Product
        fields = "__all__"