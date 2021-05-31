from django import forms
from django.forms import ModelForm
from .models import Product, Order

def is_valid_amount(form_amount, model_multiply):
    return form_amount % model_multiply == 0

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
    """
    def clean_amount_value(self):
        data = self.cleaned_data.get('amount')
    """