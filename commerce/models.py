from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Product(models.Model):
    """Model of the products being sold"""
    product_name = models.CharField("Product", max_length=100, blank=False, null=False)
    unit_price = models.FloatField("Unit Price (R$)", validators=[MinValueValidator(10.0), MaxValueValidator(10000000.0)], blank=False, null=False)
    multiple = models.IntegerField("Multiple")

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.product_name
# Create your models here.
