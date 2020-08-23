from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, RetrieveAPIView

from users.apiv1.serializers.users_serializer import UserAccountSerializer

class UserListAPIView(ListAPIView):
    queryset = UserAccount.objects.all().order_by('-pk')
    serializer_class = UserAccountSerializer


