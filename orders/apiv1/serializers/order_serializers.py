from rest_framework import serializers
from rest_framework.serializers import  ModelSerializer
from orders.models import Order, Cart, cartItem
from products.apiv1.serializers.product_seriliazers import ProductSerializer

class CartSerializer(ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    # products = ProductSerializer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    product = ProductSerializer()
    class Meta:
        model = cartItem
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    order_items = CartItemSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'