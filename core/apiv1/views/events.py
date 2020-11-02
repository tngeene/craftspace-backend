from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from core.apiv1.serializers.events_serializer import EventSerializer
from ..permissions import IsOwnerorAdmin
from core.models import Event


class EventCreateAPIView(CreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(uploaded_by=user)

class EventListAPIView(ListAPIView):
    queryset = Event.objects.filter(is_approved=True)
    serializer_class = EventSerializer
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_fields = ['uploaded_by',]


class EventRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = [IsOwnerorAdmin]

    def perform_update(self, serializer):
        instance = serializer.save()
