from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('', include('core.urls')),
    path('', include('register.urls')),
    path('', include('commerce.urls')),
    path('admin/', admin.site.urls),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
