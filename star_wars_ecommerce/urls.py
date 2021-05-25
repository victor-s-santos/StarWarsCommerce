from django.contrib import admin
from django.urls import path, include
#register imports
from register import views as v

urlpatterns = [
    #--register--#
    path('register/', v.register, name='register'),
    path('admin/', admin.site.urls),
]
