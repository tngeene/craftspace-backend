from core.models import Event
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView
from orders.models import CustomOrder, Order
from products.models import Product
from users.models import ArtistProfile
from .dashboard import DashboardView

User = get_user_model()


class ArtistListView(DashboardView, ListView):
    model = User
    context_object_name = 'users'
    queryset = User.objects.filter(membership_type='Artist')
    template_name = 'dashboard/users/artists/list.html'


class ArtistDetailView(DashboardView, DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'dashboard/users/artists/details.html'

    def get_context_data(self, **kwargs):
        artist = self.object.id
        context = super().get_context_data(**kwargs)
        context["events"] = Event.objects.filter(uploaded_by=artist)
        context["products"] = Product.objects.filter(uploaded_by=artist)
        context["custom_orders"] = CustomOrder.objects.filter(artist=artist)
        context["orders"] = Order.objects.filter(user=artist)
        context["profile"] = ArtistProfile.objects.get(user=artist)
        return context

class ArtistUpdateView(DashboardView, UpdateView):
    model = User
    fields = ('first_name','last_name',)
    template_name = 'dashboard/users/artists/edit.html'

    def get_success_url(self):
        messages.success(self.request, "Artist Details Updated")
        return reverse_lazy("dashboard:artist_details", kwargs = {'pk': self.object.pk})
