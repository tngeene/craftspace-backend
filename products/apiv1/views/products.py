from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from products.apiv1.serializers.product_seriliazers import ProductSerializer
from products.apiv1.serializers.category_serializers import CategorySerializer
from ..permissions import IsArtistOrDisallow
from products.models import Product, Category

# class ProductsAPIView(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     http_method_name = ['get','post','head', 'put','patch',]
#     permission_classes = [IsArtistOrDisallow,IsAuthenticated]

#     def perform_create(self, serializer):
#         user = self.request.user
#         return serializer.save(uploaded_by=user)

class ProductDetailsAPIView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsArtistOrDisallow, IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(uploaded_by=user)

class ProductUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()

class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

class ProductDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def perform_destroy(self, serializer):
        instance = serializer.save()
class CategoryAPIView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_name = ['get','post','head', 'put','patch',]
    permission_classes = [IsAdminUser]
