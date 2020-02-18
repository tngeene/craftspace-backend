from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..permissions import IsArtistOrDissallow
from users.apiv1.serializers.artists_serializer import ArtistProfileSerializer
from users.models import ArtistProfile

class ArtistProfileApiView(ModelViewSet):
    queryset = ArtistProfile.objects.all()
    serializer_class = ArtistProfileSerializer
    http_method_names = ['get','post','options','head','put','patch',]
    permission_classes = [IsArtistOrDissallow,IsAuthenticated]
