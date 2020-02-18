from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from products.models import Product

class ProductSerializer(ModelSerializer):
    uploaded_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Product
        fields = "__all__"