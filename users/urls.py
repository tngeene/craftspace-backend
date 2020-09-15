from django.urls import path, include

app_name = "users_api"

urlpatterns = [
    path('artists/', include('users.apiv1.urls.artists')),
    path('collectors/', include('users.apiv1.urls.collectors')),
    path('auth/custom-users/', include('users.apiv1.urls.users'))
]
