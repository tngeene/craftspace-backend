from django.contrib.auth import get_user_model
from products.models import Product
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .category_serializers import CategorySerializer

User = get_user_model()


class ProductSerializer(ModelSerializer):
    uploaded_by = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField()
    file_type = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_file_type(self, obj):
        file_type = obj.file_type
        return file_type

# retrives details of user that uploaded product


class ProductArtistSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')

# to be used in detail view of a product


class ProductDetailSerializer(ModelSerializer):
    uploaded_by = ProductArtistSerializer()
    category = CategorySerializer()
    file_type = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'picture', 'description', 'spin_image',
                  'price', 'file_type', 'uploaded_by', 'category', 'created_on')

    def get_file_type(self, obj):
        file_type = obj.file_type
        return file_type


class ProductUploadSerializer(ModelSerializer):
    uploaded_by = serializers.StringRelatedField(read_only=True)
    # category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = "__all__"
