from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders.apiv1.views.orders import OrderPostView, OrderAPIView, CartItemView

router = DefaultRouter()
router.register('orders',OrderAPIView,basename='orders'),
router.register('cart-items',CartItemView,basename='cart-items'),


urlpatterns = [
    path('',include(router.urls)),
    path('orders/add',OrderPostView.as_view()),
]
