from django_filters import rest_framework as filters
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import AllowAny

from orders.apiv1.serializers.custom_orders import (
    CustomOrderCreateSerializer, CustomOrderDetailSerializer)

from ...models import CustomOrder


class CustomOrderListCreateAPIView(ListCreateAPIView):
    permission_classes = [AllowAny]
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_fields = ['requested_by', 'artist']
    queryset = CustomOrder.objects.all()
    serializer_class = CustomOrderCreateSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomOrderDetailSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        data = self.request.data
        user = self.request.user

        if 'requested_by' in data.keys():
            return serializer.save(requested_by=user, email=user.email, phone_number=user.phone_number)
        return serializer.save()




class CustomOrderRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CustomOrder.objects.all()
    serializer_class = CustomOrderDetailSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return super().get_serializer_class()
        return CustomOrderCreateSerializer
