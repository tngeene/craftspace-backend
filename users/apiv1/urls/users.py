from django.urls import path
from ..views.users import UserListAPIView, UserDetailAPIView

urlpatterns = [
    path('', UserListAPIView.as_view(), name='users_list'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='user_details')
]
