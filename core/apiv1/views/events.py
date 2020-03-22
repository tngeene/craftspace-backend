from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from core.apiv1.serializers.events_serializer import EventSerializer
from ..permissions import IsArtistOrDissallow
from core.models import Event

# class EventsApiView(ModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#     http_method_names = ['get','post','options','head','put','patch',]
#     permission_classes = [IsArtistOrDissallow,IsAuthenticated]

#     def perform_create(self, serializer):
#         user = self.request.user
#         return serializer.save(uploaded_by=user)

class EventCreateAPIView(CreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(uploaded_by=user)

class EventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save()