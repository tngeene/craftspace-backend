from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from products.models import Product
from .category_serializers import CategorySerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class ProductSerializer(ModelSerializer):
    uploaded_by = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = "__all__"

# retrives details of user that uploaded product
class ProductArtistSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name')

# to be used in detail view of a product
class ProductDetailSerializer(ModelSerializer):
    uploaded_by = ProductArtistSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id','name','picture','description','spin_image','price','uploaded_by','category','created_on')


class ProductUploadSerializer(ModelSerializer):
    uploaded_by = serializers.StringRelatedField(read_only=True)
    # category = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = "__all__"