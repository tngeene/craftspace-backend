from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('auth/logout',
         LogoutView.as_view(template_name='account/login.html'), name='dashboard_logout'),
    path('', LoginView.as_view(template_name='account/login.html', redirect_authenticated_user=True),
         name='login'),

    # API urls
    path('api/v1/',include('users.urls')),
    path('api/v1/',include('core.apiv1.urls')),
    path('api/v1/art-pieces/',include('products.apiv1.urls')),
    path('api/v1/',include('orders.apiv1.urls')),
    path('api/v1/',include('payments.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    # dashboard url
    path('dashboard/',include('dashboard.urls',namespace='dashboard'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

