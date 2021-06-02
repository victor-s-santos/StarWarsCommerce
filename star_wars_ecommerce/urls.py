from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
#auth views
from django.contrib.auth import views as auth_views
from django.urls import path, include
#register imports
from register import views as v
#core imports
from core import views as core_v
#commerce imports
from commerce import views as commerce_v

urlpatterns = [
    path('', core_v.home, name='home'),
    #--register--#
    path('register/', v.register, name='register'),
    path('register/infos/', v.profile, name='profile'),
    #--login--#
    path('', include('django.contrib.auth.urls'), name='login'),#using only this url from this include
    #--reset_password--#
    path('register/reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset/password_reset.html"), name="reset_password"),
    path('register/reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset/password_reset_sent.html"), name="password_reset_done"),
    path('register/reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name='password_reset_confirm'),
    path('register/reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset/password_reset_complete.html"), name="password_reset_complete"),
    #--commerce--#
    path('commerce/', commerce_v.product_list, name='product_list'),
    path('commerce/product_list/<int:pk>/', commerce_v.detail_product, name='detail_product'),
    path('commerce/product_list/<pk>/remove/', commerce_v.product_remove, name='product_remove'),
    path('commerce/product_list/<int:pk>/edit/', commerce_v.product_edit, name='product_edit'),
    path('commerce/register_product/', commerce_v.product_register, name='product_register'),
    path('commerce/register_order/', commerce_v.register_order, name='product_order'),
    path('commerce/order_list/', commerce_v.order_list, name='order_list'),
    path('commerce/order_list/<int:pk>/', commerce_v.order_detail, name='order_detail'),
    path('commerce/order_list/<int:pk>/edit/', commerce_v.order_edit, name='order_edit'),
    path('commerce/order_list/<int:pk>/remove/', commerce_v.order_remove, name='order_remove'),
    #--admin--#
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
