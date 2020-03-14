from rest_framework import serializers
from rest_framework.serializers import  ModelSerializer
from orders.models import Order, Cart

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
