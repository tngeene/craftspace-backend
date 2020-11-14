from django.views.generic import ListView, DetailView

from products.models import Product
from orders.models import Order, CustomOrder, CartItem
from .dashboard import DashboardView

class OrderListView(DashboardView, ListView):
    model = Order
    template_name = 'dashboard/orders/list.html'
    context_object_name = 'orders'

class OrderDetailView(DashboardView, DetailView):
    model = Order
    conxtex_object_name = 'order'
    template_name = 'dashboard/orders/details.html'


class CustomOrderListView(DashboardView, ListView):
    model = CustomOrder
    template_name = 'dashboard/orders/custom-orders/list.html'
    context_object_name = 'orders'

class CustomOrderDetailView(DashboardView, DetailView):
    model = CustomOrder
    context_object_name = 'order'
    template_name = 'dashboard/orders/custom-orders/details.html'

