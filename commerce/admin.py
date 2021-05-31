from django.contrib import admin
from .models import Product, Order

class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    list_display = ['product_name', 'unit_price', 'multiple', 'published_date']
    search_fields = ['product_name', 'unit_price', 'multiple', 'published_date']
    list_filter = ['product_name', 'unit_price', 'multiple', 'published_date']

class OrderAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    list_display = ['user','product_name', 'suggested_price', 'amount','published_date']
    search_fields = ['user','product_name', 'suggested_price', 'amount','published_date']
    list_filter = ['user','product_name', 'suggested_price', 'amount','published_date']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
