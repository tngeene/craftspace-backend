from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders.apiv1.views.orders import OrderPostView, OrderDetailsAPIView, CartItemView, OrderListAPIView
from orders.apiv1.views.custom_orders import CustomOrderListCreateAPIView,CustomOrderRUDAPIView
router = DefaultRouter()

router.register('cart-items',CartItemView,basename='cart-items'),


app_name = 'orders_api'

urlpatterns = [
    path('',include(router.urls)),
    path('orders/add',OrderPostView.as_view(),name='add_orders'),
    path('orders/<int:pk>/details/',OrderDetailsAPIView.as_view(),name='order_details'),
    path('orders/my-orders/',OrderListAPIView.as_view(),name='logged_in_user_oders'),

    # custom orders endpoints
    path('custom-orders/',CustomOrderListCreateAPIView.as_view(),name='add_custom_orders'),
    path('custom-orders/<int:pk>/',CustomOrderRUDAPIView.as_view(),name='custom_orders_rud'),
]
