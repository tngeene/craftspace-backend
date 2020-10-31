from django.contrib.auth import get_user_model
from rest_framework.generics import (ListAPIView, RetrieveAPIView, CreateAPIView,
                                     RetrieveUpdateAPIView)
from rest_framework.permissions import AllowAny

from users.apiv1.serializers.users_serializer import CustomUserSerializer, UserRegistrationSerializer

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all().order_by('-pk')
    serializer_class = CustomUserSerializer


class UserDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
