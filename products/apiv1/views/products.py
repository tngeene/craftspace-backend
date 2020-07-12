from django_filters import rest_framework as filters
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     ListCreateAPIView, RetrieveAPIView,
                                     RetrieveDestroyAPIView,
                                     RetrieveUpdateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from products.apiv1.serializers.category_serializers import (
    CategoryDetailSerializer, CategorySerializer)
from products.apiv1.serializers.product_seriliazers import (
    ProductDetailSerializer, ProductSerializer, ProductUploadSerializer)
from products.models import Category, Product

from ..permissions import IsArtistOrDisallow

# class ProductsAPIView(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     http_method_name = ['get','post','head', 'put','patch',]
#     permission_classes = [IsArtistOrDisallow,IsAuthenticated]

#     def perform_create(self, serializer):
#         user = self.request.user
#         return serializer.save(uploaded_by=user)

class ProductDetailsAPIView(RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()

class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductUploadSerializer
    permission_classes = [IsArtistOrDisallow, IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(uploaded_by=user)

class ProductUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = ProductUploadSerializer
    queryset = Product.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()

class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_fields = ['category','uploaded_by']

    def get_queryset(self):
        return Product.objects.all()

class ProductDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsArtistOrDisallow,IsAdminUser]


class CategoryAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_fields = ['name']
    # permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategoryDetailSerializer
        return super().get_serializer_class()

class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategoryDetailSerializer
        return super().get_serializer_class()
