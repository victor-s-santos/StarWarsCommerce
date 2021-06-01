from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

class Product(models.Model):
    """Model of the products being sold"""
    product_name = models.CharField("Product", max_length=100, blank=False, null=False)
    unit_price = models.FloatField("Unit Price (R$)", validators=[MinValueValidator(10.0), MaxValueValidator(10000000.0)], blank=False, null=False)
    multiple = models.IntegerField("Multiple", default=1, null=True, blank=True)
    published_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.product_name

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=False)
    product_name = models.ForeignKey(Product, unique=False, on_delete=models.CASCADE)
    suggested_price = models.FloatField("Suggested Price (R$)", validators=[MinValueValidator(10.0), MaxValueValidator(10000000.0)], blank=False, null=False)
    amount = models.IntegerField("Amount", default=1, null=True, blank=True)
    published_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return str(self.user.first_name) + ' -> ' + str(self.product_name)
