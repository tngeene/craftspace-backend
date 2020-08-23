from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters
from rest_framework.generics import (ListAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated

from users.apiv1.serializers.artists_serializer import (
    ArtistProfileCreateSerializer, ArtistProfileDetailSerializer,
    ArtistProfileListSerializer)
from users.models import ArtistProfile

from ..permissions import IsArtistOrDissallow, IsOwnerOrReadOnly
from ..serializers.users_serializer import UserAccountSerializer

User = get_user_model()

class ArtistListAPIView(ListAPIView):
    queryset = User.objects.filter(membership_type='Artist').order_by('-pk')
    serializer_class = UserAccountSerializer

class ArtistProfileCreateAPIView(ListCreateAPIView):
    queryset = ArtistProfile.objects.all()
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_fields = ['user',]
    serializer_class = ArtistProfileCreateSerializer
    permission_classes = [IsArtistOrDissallow, IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(user=user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArtistProfileListSerializer
        return super().get_serializer_class()

class ArtistProfileRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ArtistProfileCreateSerializer
    queryset = ArtistProfile.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArtistProfileDetailSerializer
        return super().get_serializer_class()
