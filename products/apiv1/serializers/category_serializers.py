from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from products.models import Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"