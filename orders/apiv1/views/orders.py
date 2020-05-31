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
from payments.mpesa_credentials import MpesaAccessToken, LipaNaMpesaPassword
import json
import requests

from orders.models import Order, Cart, CartItem
from products.models import Product
from payments.models import MpesaPayment

class CartItemView(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class  = CartItemSerializer

class OrderAPIView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # GET for admin, POST for collectors
    permission_classes = [IsAuthenticated,IsCollectorOrIsAdmin,]


# mpesa variables
access_token = MpesaAccessToken.validated_mpesa_access_token
# print(f"access token is {access_token}")
api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
class OrderPostView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request, **kwargs):

        headers = {"Authorization": "Bearer %s" % access_token} #mpesa header with access token
        data = request.data
        # checks if a client is registered in the system, if not sets the client value to null
        if self.request.user.is_anonymous:
            order = Order.objects.create(phone_number=data['phone_number'],order_total=data['order_total'])
        # mpesa logic
            request = {
                "BusinessShortCode": LipaNaMpesaPassword.business_shortcode,
                "Password": LipaNaMpesaPassword.decode_password,
                 "Timestamp": LipaNaMpesaPassword.lipa_time,
                 "TransactionType": "CustomerPayBillOnline",
                 "Amount": data['order_total'],
                 "PartyA": data['phone_number'],  # phone number getting stk push
                 "PartyB": LipaNaMpesaPassword.business_shortcode,  #business till no.or paybill
                 "PhoneNumber": data['phone_number'], # phone number getting stk push same as party A
                 "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
                 "AccountReference": "Craftspace",
                 "TransactionDesc": "Testing stk push"
                }
            response = requests.post(api_url, json=request, headers=headers)
            print(f"response is {response.text}")
            print(f"response body is {response.body}")
            print(f"request is {request}")
        else:
            order = Order.objects.create(user=self.request.user,
            phone_number=data['phone_number'],order_total=data['order_total'])

            print(f"order total {order.order_total}")
        # mpesa logic
            request = {
                "BusinessShortCode": LipaNaMpesaPassword.business_shortcode,
                "Password": LipaNaMpesaPassword.decode_password,
                 "Timestamp": LipaNaMpesaPassword.lipa_time,
                 "TransactionType": "CustomerPayBillOnline",
                 "Amount": data['order_total'],
                 "PartyA": data['phone_number'],  # phone number getting stk push
                 "PartyB": LipaNaMpesaPassword.business_shortcode,  #business till no.or paybill
                 "PhoneNumber": data['phone_number'], # phone number getting stk push same as party A
                 "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
                 "AccountReference": "Craftspace",
                 "TransactionDesc": "Testing stk push"
                }
            response = requests.post(api_url, json=request, headers=headers)
           

        # saving the processed order payment to db
        # mpesa_body = request.decode('utf-8')
        # mpesa_payment = json.loads(mpesa_body)
        # payment = MpesaPayment.objects.create(
        #     first_name = mpesa_payment['FirstName'],
        #     last_name=mpesa_payment['LastName'],
        #     middle_name=mpesa_payment['MiddleName'],
        #     order = order,
        #     description=mpesa_payment['TransID'],
        #     phone_number=mpesa_payment['MSISDN'],
        #     amount=mpesa_payment['TransAmount'],
        #     reference=mpesa_payment['BillRefNumber'],
        #     organization_balance=mpesa_payment['OrgAccountBalance'],
        #     transaction_type=mpesa_payment['TransactionType'],
        # )


        #processing order times and saving to db
        order_items = data['order_items']
        print(f"order items are {order_items}")
        for item in order_items:
            print(f"items in cart are {item['product']['id']}")
            cart_product = get_object_or_404(Product, id=item['product']['id'])
            print(f'cart prod is {cart_product}')
            if self.request.user.is_anonymous:
                cart_items = CartItem.objects.create(product=cart_product,quantities=item['product']['quantities'])
            else:
                cart_items = CartItem.objects.create(product=cart_product,quantities=item['product']['quantities'],owner=self.request.user)
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
    