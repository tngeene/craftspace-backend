from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.apiv1.views.products import ProductsAPIView, CategoryAPIView

router = DefaultRouter()
router.register('art-pieces', ProductsAPIView,base_name='art_pieces')
router.register('art-categories', CategoryAPIView,base_name='art_categories')

urlpatterns = [
    path('',include(router.urls))
]

