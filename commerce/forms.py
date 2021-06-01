from django import forms
from django.forms import ModelForm
from .models import Product, Order
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


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

    def clean(self):
        cleaned_data = super().clean()
        amount = cleaned_data['amount']
        suggested_price = cleaned_data['suggested_price']
        multiple = cleaned_data['product_name'].multiple
        unit_price = cleaned_data['product_name'].unit_price
        if amount % multiple:
            raise ValidationError(_("Quantity %(amount)s is not multiple of %(multiple)s"),
                params={"amount": amount, "multiple": multiple},
                code="invalid_amount_value",
                )
        if not (suggested_price > unit_price * 0.9):
            raise ValidationError(_("Suggested Price %(suggested_price)s is less than 90 %% of Unit Price %(unit_price)s."),
                params={"suggested_price": suggested_price, "unit_price": unit_price},
                code="invalid_suggested_price_value",
                )