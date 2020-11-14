from core.models import Event
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .dashboard import DashboardView


class EventCreateView(DashboardView, CreateView):
    model = Event
    fields = ('name', 'description', 'date',
              'venue', 'ticket_price', 'banner',)
    template_name = 'dashboard/events/add.html'

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "Event Successully Created")
        return reverse_lazy("dashboard:event_details", kwargs={'pk': self.object.pk})


class EventUpdateView(DashboardView, UpdateView):
    model = Event
    fields = ('name', 'description', 'date',
              'venue', 'ticket_price', 'banner',)
    template_name = 'dashboard/events/edit.html'

    def get_success_url(self):
        messages.success(self.request, "Event Successully Updated")
        return reverse_lazy("dashboard:event_details", kwargs={'pk': self.object.pk})


class EventDetailView(DashboardView, DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'dashboard/events/details.html'


class EventListView(DashboardView, ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'dashboard/events/list.html'
