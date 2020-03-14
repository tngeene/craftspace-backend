from rest_framework import generics, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from orders.apiv1.serializers.order_serializers import CartSerializer, OrderSerializer
from ..permissions import IsCollectorOrIsAdmin

from orders.models import Order, Cart

class OrderAPIView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # GET for admin, POST for collectors
    permission_classes = [IsAuthenticated,IsCollectorOrIsAdmin,]

class CartListAPIView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    

# class CartItemListAPIView(generics.ListAPIView):
#     queryset = CartItem.objects.all()
#     serializer_class = CartIemSerializer
#     permission_classes = [IsAuthenticated]
    