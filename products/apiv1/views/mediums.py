from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from ...models import Medium
from ..serializers.mediums import MediumSerializer


class MediumListCreateAPIView(ListCreateAPIView):
    queryset = Medium.objects.all()
    serializer_class = MediumSerializer

