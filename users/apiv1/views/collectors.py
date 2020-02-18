from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ..permissions import IsCollectorOrDissallow
from users.models import CollectorProfile
from users.apiv1.serializers.collectors_serializer import CollectorProfileSerializer

class CollectorProfileApiView(ModelViewSet):
    queryset = CollectorProfile.objects.all()
    serializer_class = CollectorProfileSerializer
    http_method_names = ['get','post','options','head','put','patch',]
    permission_classes = [IsCollectorOrDissallow,IsAuthenticated]