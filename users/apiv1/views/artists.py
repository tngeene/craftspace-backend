from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from ..permissions import IsArtistOrDissallow, IsOwnerOrReadOnly
from users.apiv1.serializers.artists_serializer import ArtistProfileSerializer
from users.models import ArtistProfile

class ArtistProfileApiView(ModelViewSet):
    queryset = ArtistProfile.objects.all()
    serializer_class = ArtistProfileSerializer
    http_method_names = ['get','post','options','head','put','patch',]


class ArtistProfileCreateAPIView(CreateAPIView):
    serializer_class = ArtistProfileSerializer
    permission_classes = [IsArtistOrDissallow, IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(user=user)


class ArtistProfileUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ArtistProfileSerializer
    queryset = ArtistProfile.objects.all()

class ArtistProfileListAPIView(ListAPIView):
    serializer_class = ArtistProfileSerializer
    queryset = ArtistProfile.objects.all()
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_fields = ['user',]

class ArtistProfileDetailView(RetrieveAPIView):
    serializer_class  = ArtistProfileSerializer