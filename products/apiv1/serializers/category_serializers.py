from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from products.models import Category, Product

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

# will be used in the detail view of a category
class ProductCategorySerializer(ModelSerializer):
    uploaded_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Product
        fields = ('id','name','picture','name','uploaded_by')


class CategoryDetailSerializer(ModelSerializer):
    products = ProductCategorySerializer(many=True)
    class Meta:
        model = Category
        fields = ('id','name','cover_photo','products')
