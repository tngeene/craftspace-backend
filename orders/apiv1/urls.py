from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders.apiv1.views.orders import OrderPostView, OrderAPIView, CartItemView
from orders.apiv1.views.custom_orders import CustomOrderListCreateAPIVIew,CustomOrderRUDAPIView
router = DefaultRouter()
router.register('orders',OrderAPIView,basename='orders'),
router.register('cart-items',CartItemView,basename='cart-items'),


app_name = 'orders_api'

urlpatterns = [
    path('',include(router.urls)),
    path('orders/add',OrderPostView.as_view(),name='add_orders'),

    # custom orders endpoints
    path('custom-orders/',CustomOrderListCreateAPIVIew.as_view(),name='add_custom_orders'),
    path('custom-orders/<int:pk>',CustomOrderRUDAPIView.as_view(),name='custom_orders_rud'),
]
