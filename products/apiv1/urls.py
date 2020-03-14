from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.apiv1.views.products import ProductCreateAPIView, ProductUpdateAPIView, ProductListAPIView, ProductDestroyAPIView, \
    CategoryAPIView, ProductDetailsAPIView

router = DefaultRouter()
# router.register('art-pieces', ProductsAPIView,basename='art_pieces')
router.register('art-categories', CategoryAPIView,basename='art_categories')

urlpatterns = [
    path('',include(router.urls)),
    path('all-art-pieces/',ProductListAPIView.as_view(),name='all_pieces'),
    path('add/', ProductCreateAPIView.as_view(),name='product_add'),
    path('<int:pk>/edit/', ProductUpdateAPIView.as_view(),name='product_edit'),
    path('<int:pk>/', ProductDetailsAPIView.as_view(),name='product_details'),
    path('<int:pk>/delete/', ProductDestroyAPIView.as_view(),name='product_destroy'),
]

