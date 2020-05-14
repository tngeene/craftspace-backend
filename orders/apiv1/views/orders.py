from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_201_CREATED, HTTP_202_ACCEPTED 
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from orders.apiv1.serializers.order_serializers import CartSerializer, OrderSerializer, CartItemSerializer
from ..permissions import IsCollectorOrIsAdmin
from django.shortcuts import get_object_or_404


from orders.models import Order, Cart, cartItem
from products.models import Product

class CartItemView(ModelViewSet):
    queryset = cartItem.objects.all()
    serializer_class  = CartItemSerializer

class OrderAPIView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # GET for admin, POST for collectors
    permission_classes = [IsAuthenticated,IsCollectorOrIsAdmin,]



class OrderPostView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request, **kwargs):
        data = request.data
        order_items = data['products']

        for item in order_items:
            cart_items = get_object_or_404(Product, item)
            order = Order.objects.create(status=data['status'],user=data['user'],
            phone_number=data['phone_number'],order_total=data['order_total'])
            order.order_items.add(cart_items)
            order.save()
        return Response(status=status.HTTP_200_OK)


class CartListAPIView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

class CartCreateAPIView(CreateAPIView):
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        user = self.request.user
        item = self.request.data
        # return serializer.save(owner=user)

        product = get_object_or_404(Product, id=item["item"])

        order_qs = Order.objects.filter(user=user, status="placed")

        if order_qs.exists():
            order = order_qs.first()
            if order.order_items.filter(item__id=product.id).exists():
                cart_item = order.order_items.get(item__id=product.id)
                cart_item.number_of_items += serializer.validated_data["number_of_items"]
                cart_item.set_total_price()
                order.total_price()
                return Response(
                    "This item quantity was updated to your cart",
                    status=HTTP_202_ACCEPTED,
                )
            else:
                serializer.save()
                order.order_items.add(serializer.instance)
                serializer.instance.set_total_price()
                order.total_price()
                Response("Item added to cart", status=HTTP_201_CREATED)
        else:
            order = Order.objects.create(user=user)
            serializer.save()
            order.order_items.add(serializer.instance)
            serializer.instance.set_total_price()
            order.total_price()
            Response("Item added to cart", status=HTTP_201_CREATED)

class CartRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    # def perform_update(self, serializer):
    #     user = self.request.user
    #     return super().perform_update(serializer)


    # def perform_destroy(self, instance):
    #     user = self.request.user
    #     print(instance)
    #     item = instance.data

    #     product = get_object_or_404(Product, id=item["item"])

    #     cart_qs = Cart.objects.filter(user=user, item=item)

    #     order_qs = Order.objects.filter(user=user, status="placed")

    #     if cart_qs.exists():
    #         cart = cart_qs.last()
    #         cart.delete()
    #         order = order_qs.last()
    #         order.total_price()
    #     return super().perform_destroy(instance)

# class CartItemListAPIView(generics.ListAPIView):
#     queryset = CartItem.objects.all()
#     serializer_class = CartIemSerializer
#     permission_classes = [IsAuthenticated]
    