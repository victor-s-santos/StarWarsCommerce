from django.contrib import admin
from django.urls import path, include
#register imports
from register import views as v
#core imports
from core import views as core_v

urlpatterns = [
    path('', core_v.home, name='home'),
    #--register--#
    path('register/', v.register, name='register'),
    path('admin/', admin.site.urls),
]
