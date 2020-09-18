from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.generics import (ListAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.apiv1.serializers.artists_serializer import (
    ArtistProfileCreateSerializer, ArtistProfileDetailSerializer,
    ArtistProfileListSerializer)
from users.models import ArtistProfile, Rating

from ..permissions import IsArtistOrDissallow, IsOwnerOrReadOnly
from ..serializers.users_serializer import UserAccountSerializer

User = get_user_model()


class ArtistListAPIView(ListAPIView):
    queryset = User.objects.filter(membership_type='Artist', is_active=True).order_by('-pk')
    serializer_class = UserAccountSerializer


class ArtistProfileCreateAPIView(ListCreateAPIView):
    queryset = ArtistProfile.objects.all()
    filter_backends = [filters.DjangoFilterBackend, ]
    filterset_fields = ['user', ]
    serializer_class = ArtistProfileCreateSerializer

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

    def perform_update(self, serializer):
        user = self.request.user
        return serializer.save(user=user)

# post a rating for an artist profile
class RatingPostAPIView(APIView):
    def post(self, *args, **kwargs):
        user = self.request.user
        data = self.request.data
        rating_value = data['rating']
        profile_id = data['profile']

        profile = ArtistProfile.objects.get(id=profile_id)
        # ensure that only logged in users can post a rating
        if not user.is_anonymous:
            rating, created = Rating.objects.get_or_create(
                rating=rating_value, artist_profile=profile, posted_by=user)
            rating.save()

            return Response({"detail": "Rating posted, thanks for your feedback!"}, status=status.HTTP_201_CREATED)
        return Response({"detail": "Please login or Create an account to rate artist 😕"}, status=status.HTTP_403_FORBIDDEN)
