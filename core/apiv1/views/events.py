from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.apiv1.serializers.events_serializer import EventSerializer
from ..permissions import IsArtistOrDissallow
from core.models import Event

class EventsApiView(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    http_method_names = ['get','post','options','head','put','patch',]
    permission_classes = [IsArtistOrDissallow,IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(uploaded_by=user)