from django.urls import path
from core import views as core_v

app_name = 'core'
urlpatterns = [
    path('', core_v.home, name='home'),
]
