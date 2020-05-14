from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders.apiv1.views.orders import OrderPostView, OrderAPIView, CartListAPIView, CartCreateAPIView, CartRetrieveUpdateDestroyView, \
    CartItemView

router = DefaultRouter()
router.register('orders',OrderAPIView,basename='orders'),
router.register('cart-items',CartItemView,basename='cart-items'),


urlpatterns = [
    path('',include(router.urls)),
    path('orders/add',OrderPostView.as_view()),
    path('carts/',CartListAPIView.as_view()),
    path('cart/add/', CartCreateAPIView.as_view()),
    path('cart/<int:pk>',CartRetrieveUpdateDestroyView.as_view())
    # path('orders/carts/items',CartItemListAPIView.as_view(),)
]
