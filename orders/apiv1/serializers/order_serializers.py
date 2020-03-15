from rest_framework import serializers
from rest_framework.serializers import  ModelSerializer
from orders.models import Order, Cart

class OrderSerializer(ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Order
        fields = '__all__'

class CartSerializer(ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Cart
        fields = '__all__'
