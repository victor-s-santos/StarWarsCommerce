from django.urls import path
from commerce import views as commerce_v

urlpatterns = [
    path('commerce/', commerce_v.product_list, name='product_list'),
    path('commerce/product_list/<int:pk>/', commerce_v.detail_product, name='detail_product'),
    path('commerce/product_list/<pk>/remove/', commerce_v.product_remove, name='product_remove'),
    path('commerce/product_list/<int:pk>/edit/', commerce_v.product_edit, name='product_edit'),
    path('commerce/register_product/', commerce_v.product_register, name='product_register'),
    path('commerce/register_order/', commerce_v.register_order, name='register_order'),
    path('commerce/order_list/', commerce_v.order_list, name='order_list'),
    path('commerce/order_list/<int:pk>/', commerce_v.order_detail, name='order_detail'),
    path('commerce/order_list/<int:pk>/edit/', commerce_v.order_edit, name='order_edit'),
    path('commerce/order_list/<int:pk>/remove/', commerce_v.order_remove, name='order_remove'),
]
