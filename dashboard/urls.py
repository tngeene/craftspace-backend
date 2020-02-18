from django.urls import path

from dashboard.views.dashboard import DashboardTemplateView

app_name = 'dashboard'

urlpatterns = [
    path('',DashboardTemplateView.as_view(),name='index'),
]
