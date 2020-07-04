from rest_framework import serializers
from rest_framework.serializers import  ModelSerializer
from orders.models import Order, CartItem
from products.apiv1.serializers.product_seriliazers import ProductSerializer

class CartItemSerializer(ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    order_items = CartItemSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'