from django.views.generic import DetailView, ListView

from core.models import Feedback

from ..views.dashboard import DashboardView


class FeedbackListView(DashboardView, ListView):
    model = Feedback
    template_name = 'dashboard/feedback/list.html'
    context_object_name = 'feedbacks'
    queryset = Feedback.objects.all().order_by('-created_on')


class FeedbackDetailView(DashboardView, DetailView):
    model = Feedback
    template_name = 'dashboard/feedback/details.html'
    context_object_name = 'feedback'
