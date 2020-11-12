from orders.models import CartItem, Order
from products.apiv1.serializers.product_seriliazers import ProductSerializer
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class CartItemSerializer(ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = '__all__'


class OrderListSerializer(ModelSerializer):
    order_items_count = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'user', 'status', 'first_name', 'last_name', 'email',
                  'phone_number', 'order_total', 'order_items_count', 'order_date',)

    def get_order_items_count(self, obj):
        cart_items = obj.order_items.count()
        if cart_items > 0:
            return cart_items
        elif cart_items < 1:
            return 0


class OrderSerializer(ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    order_items = CartItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
