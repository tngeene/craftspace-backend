from django.contrib.auth import get_user_model
from rest_framework.generics import (ListAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.apiv1.serializers.collectors_serializer import \
    CollectorProfileSerializer, CollectorProfileDetailSerializer
from users.models import CollectorProfile
from django_filters import rest_framework as filters
from ..permissions import IsCollectorOrDissallow
from ..serializers.users_serializer import UserAccountSerializer

User = get_user_model()


class CollectorsListAPIView(ListAPIView):
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields =  ['user']
    queryset = User.objects.filter(membership_type='Collector').order_by('-pk')
    serializer_class = UserAccountSerializer



class CollectorProfileListCreateAPIView(ListCreateAPIView):
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields =  ['user']
    queryset = CollectorProfile.objects.all()
    serializer_class = CollectorProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(user=user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CollectorProfileDetailSerializer
        return super().get_serializer_class()


class CollectorProfileRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CollectorProfile.objects.all()
    serializer_class = CollectorProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        user = self.request.user
        return serializer.save(user=user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CollectorProfileDetailSerializer
        return super().get_serializer_class()
