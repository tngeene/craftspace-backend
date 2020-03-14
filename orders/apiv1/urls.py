from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders.apiv1.views.orders import OrderAPIView, CartListAPIView

router = DefaultRouter()
router.register('orders',OrderAPIView,basename='orders'),


urlpatterns = [
    path('',include(router.urls)),
    path('orders/carts',CartListAPIView.as_view(),),
    # path('orders/carts/items',CartItemListAPIView.as_view(),)
]
