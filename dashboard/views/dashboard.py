from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from users.models import UserAccount
from core.models import Event

class DashboardView(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return True
        return False


class DashboardTemplateView(DashboardView,TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        artist = UserAccount.objects.filter(membership_type='Artist')
        collector = UserAccount.objects.filter(membership_type='Collector')
        event = Event.objects.all()
        context = super(DashboardTemplateView, self).get_context_data(**kwargs)

        
        context['collectors_count'] = UserAccount.objects.filter(membership_type ='Artist').count()
        context['artists_count'] = UserAccount.objects.filter(membership_type ='Collector').count()
        context['events_count'] = event.count()
        context['recent_artists'] = artist.order_by('-pk')[:10]
        context['recent_collectors'] = collector.order_by('-pk')[:10]
        context['recent_events'] = event.order_by('-pk')[:10]
        
        return context