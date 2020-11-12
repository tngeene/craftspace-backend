import json

import requests
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from rest_framework import generics, status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from orders.apiv1.serializers.order_serializers import (CartItemSerializer, OrderListSerializer,
                                                        OrderSerializer)
from orders.models import CartItem, Order
from payments.models import MpesaPayment
from payments.mpesa_credentials import LipaNaMpesa, MpesaAccessToken
from products.models import Product

from ..permissions import IsCollectorOrIsAdmin


class CartItemView(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class OrderDetailsAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderListAPIView(ListAPIView):
    serializer_class = OrderListSerializer
    def get_queryset(self):
        user = self.request.user
        qs = Order.objects.filter(user=user)
        return qs



# mpesa variables
access_token = MpesaAccessToken.validated_mpesa_access_token
# print(f"access token is {access_token}")
api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"


class OrderPostView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request, **kwargs):

        headers = {"Authorization": "Bearer %s" %
                   access_token}  # mpesa header with access token
        data = request.data
        # checks if a client is registered in the system, if not sets the client value to null
        if self.request.user.is_anonymous:
            order = Order.objects.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'],
                                         phone_number=data['phone_number'], order_total=data['order_total'])
        # mpesa logic
            request = {
                "BusinessShortCode": LipaNaMpesa.business_shortcode,
                "Password": LipaNaMpesa.decode_password,
                "Timestamp": LipaNaMpesa.lipa_time,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": data['order_total'],
                # phone number getting stk push
                "PartyA": data['phone_number'],
                "PartyB": LipaNaMpesa.business_shortcode,  # business till no.or paybill
                # phone number getting stk push same as party A
                "PhoneNumber": data['phone_number'],
                "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
                "AccountReference": "Craftspace",
                "TransactionDesc": "Testing stk push"
            }
            response = requests.post(api_url, json=request, headers=headers)

        else:
            order = Order.objects.create(user=self.request.user, first_name=self.request.user.first_name,
                                         last_name=self.request.user.last_name, email=self.request.user.email, phone_number=data['phone_number'], order_total=data['order_total'])

            print(f"order total {order.order_total}")
        # mpesa logic
            request = {
                "BusinessShortCode": LipaNaMpesa.business_shortcode,
                "Password": LipaNaMpesa.decode_password,
                "Timestamp": LipaNaMpesa.lipa_time,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": data['order_total'],
                # phone number getting stk push
                "PartyA": data['phone_number'],
                "PartyB": LipaNaMpesa.business_shortcode,  # business till no.or paybill
                # phone number getting stk push same as party A
                "PhoneNumber": data['phone_number'],
                "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
                "AccountReference": "Craftspace",
                "TransactionDesc": "Testing stk push"
            }
            response = requests.post(api_url, json=request, headers=headers)

            print(f"response is {response.status_code}")
            print(f"response data is {response.text}")

            if response.status_code == 200:
                return Response(status=status.HTTP_200_OK)
            elif response.status_code == 500:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        # processing order items and saving to db
        order_items = data['order_items']
        for item in order_items:
            print(f"items in cart are {item['product']['id']}")
            cart_product = get_object_or_404(Product, id=item['product']['id'])
            print(f'cart prod is {cart_product}')
            if self.request.user.is_anonymous:
                cart_items = CartItem.objects.create(
                    product=cart_product, quantities=item['product']['quantities'])
            else:
                cart_items = CartItem.objects.create(product=cart_product, quantities=item['product']['quantities'],
                                                     owner=self.request.user)
            order.order_items.add(cart_items)
            order.save()
            # send_checkout_email(order)

        return Response(status=status.HTTP_200_OK)

# def send_checkout_email(self, object):
#     current_site = get_current_site(self.request)


#     client_subject = "Invoice for order on craftspace"
#     client_message = render_to_string(
#         "emails/invoice.html",
#             {
#                 "user": object.first_name,
#                 "email": object.email,
#                 "domain": current_site.domain,
#             },
#         )
#     client_email = EmailMultiAlternatives(
#                 subject, client_message, from_email="sales@craftspace.com", to=[object.email,]
#             )

#     artist_subject = "New Order Notification"
#     artist_message = render_to_string(
#         "emails/receipt.html",
#         {
#             "user":object.
#         },
#     )
#     email.content_subtype = "html"
#     email.send()
