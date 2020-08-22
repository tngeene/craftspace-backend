from django_filters import rest_framework as filters
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.apiv1.serializers.artists_serializer import (
    ArtistProfileCreateSerializer, ArtistProfileDetailSerializer,
    ArtistProfileListSerializer)
from users.models import ArtistProfile

from ..permissions import IsArtistOrDissallow, IsOwnerOrReadOnly


class ArtistProfileCreateAPIView(CreateAPIView):
    serializer_class = ArtistProfileCreateSerializer
    permission_classes = [IsArtistOrDissallow, IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(user=user)


class ArtistProfileUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ArtistProfileCreateSerializer
    queryset = ArtistProfile.objects.all()

class ArtistProfileListAPIView(ListAPIView):
    serializer_class = ArtistProfileListSerializer
    queryset = ArtistProfile.objects.all()
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_fields = ['user',]

class ArtistProfileDetailView(RetrieveAPIView):
    queryset = ArtistProfile.objects.all()
    serializer_class  = ArtistProfileDetailSerializer
