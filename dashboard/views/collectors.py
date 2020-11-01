from core.models import Event
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView
from orders.models import CustomOrder, Order
from products.models import Product
from users.models import CollectorProfile
from .dashboard import DashboardView

User = get_user_model()


class CollectorListView(DashboardView, ListView):
    model = User
    context_object_name = 'users'
    queryset = User.objects.filter(membership_type='Collector')
    template_name = 'dashboard/users/collectors/list.html'


class CollectorDetailView(DashboardView, DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'dashboard/users/collectors/details.html'

    def get_context_data(self, **kwargs):
        collector = self.object.id
        context = super().get_context_data(**kwargs)
        context["events"] = Event.objects.filter(uploaded_by=collector)
        context["products"] = Product.objects.filter(uploaded_by=collector)
        context["custom_orders"] = CustomOrder.objects.filter(requested_by=collector)
        context["orders"] = Order.objects.filter(user=collector)
        context["profile"] = CollectorProfile.objects.get(user=collector)
        return context

class CollectorUpdateView(DashboardView, UpdateView):
    model = User
    fields = ('first_name','last_name',)
    template_name = 'dashboard/users/collectors/edit.html'

    def get_success_url(self):
        messages.success(self.request, "Collector Details Updated")
        return reverse_lazy("dashboard:collector_details", kwargs = {'pk': self.object.pk})
