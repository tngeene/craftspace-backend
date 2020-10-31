from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from core.models import Event
from products.models import Product
from orders.models import Order, CustomOrder

User = get_user_model() 
class DashboardView(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return True
        return False


class DashboardTemplateView(DashboardView,TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        artist = User.objects.filter(membership_type='Artist')
        collector = User.objects.filter(membership_type='Collector')
        event = Event.objects.all()
        orders = Order.objects.all()
        products = Product.objects.all()
        custom_orders = CustomOrder.objects.all()
        context = super(DashboardTemplateView, self).get_context_data(**kwargs)


        context['collectors_count'] = collector.count()
        context['artists_count'] = artist.count()
        context['events_count'] = event.count()
        context['orders_count'] = orders.count()
        context['custom_orders_count'] = custom_orders.count()
        context['products_count'] = products.count()
        context['recent_artists'] = artist.order_by('-pk')[:10]
        context['recent_collectors'] = collector.order_by('-pk')[:10]
        context['recent_events'] = event.order_by('-pk')[:10]
        context['recent_orders'] = orders.order_by('-pk')[:10]
        context['recent_custom_orders'] = custom_orders.order_by('-pk')[:10]
        context['recent_products'] = products.order_by('-pk')[:10]

        return context