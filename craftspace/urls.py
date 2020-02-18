from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('users.apiv1.urls')),
    path('api/v1/',include('core.apiv1.urls')),
    path('api/v1/',include('products.apiv1.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('dashboard/',include('dashboard.urls',namespace='dashboard'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)