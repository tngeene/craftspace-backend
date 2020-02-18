from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView

from users.models import UserAccount
from users.apiv1.serializers.users_serializer import UserAccountSerializer

class UserListAPIView(ListAPIView):
    queryset = UserAccount.objects.all().order_by('-pk')
    serializer_class = UserAccountSerializer

class ArtistListAPIView(UserListAPIView):
    queryset = UserAccount.objects.filter(membership_type='Artist').order_by('-pk')

class CollectorListAPIView(UserListAPIView):
    queryset = UserAccount.objects.filter(membership_type ='Collector').order_by('-pk')