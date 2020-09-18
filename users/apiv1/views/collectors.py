from django.contrib.auth import get_user_model
from rest_framework.generics import (ListAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.apiv1.serializers.collectors_serializer import \
    CollectorProfileSerializer
from users.models import CollectorProfile

from ..permissions import IsCollectorOrDissallow
from ..serializers.users_serializer import UserAccountSerializer

User = get_user_model()


class CollectorsListAPIView(ListAPIView):
    queryset = User.objects.filter(membership_type='Collector').order_by('-pk')
    serializer_class = UserAccountSerializer


class CollectorProfileListCreateAPIView(ListCreateAPIView):
    queryset = CollectorProfile.objects.all()
    serializer_class = CollectorProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(user=user)


class CollectorProfileRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CollectorProfile.objects.all()
    serializer_class = CollectorProfileSerializer
    permission_classes = [IsCollectorOrDissallow]

    def perform_update(self, serializer):
        user = self.request.user
        return serializer.save(user=user)
