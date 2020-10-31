from django.urls import path
from ..views.users import UserListAPIView, UserDetailAPIView, UserCreateAPIView

urlpatterns = [
    path('', UserListAPIView.as_view(), name='users_list'),
    path('add/', UserCreateAPIView.as_view(), name='users_add'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='user_details')
]
