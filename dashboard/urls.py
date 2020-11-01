from django.urls import path

from dashboard.views.dashboard import DashboardTemplateView

from .views.admin_actions import (UserConfirmSuspendView, activate_user,
                                  suspend_user, approve_event, reject_event)
from .views.artists import ArtistDetailView, ArtistListView, ArtistUpdateView
from .views.collectors import (CollectorDetailView, CollectorListView,
                               CollectorUpdateView)
from .views.events import (EventCreateView, EventDetailView, EventListView,
                           EventUpdateView)

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardTemplateView.as_view(), name='index'),

    # admin action urls
    path('users/<int:pk>/confirm-suspend/', UserConfirmSuspendView.as_view(), name="user_confirm_suspend"),
    path('users/<int:pk>/suspend_user/', suspend_user,name="user_suspend_action"),
    path('users/<int:pk>/unsuspend_user/', activate_user,name="user_unsuspend_action"),
    path('events/<int:pk>/reject/', reject_event, name="event_reject_action"),
    path('events/<int:pk>/approve/', approve_event, name="event_approve_action"),

    # artist urls
    path('artists/all/', ArtistListView.as_view(), name='artist_list'),
    path('artists/<int:pk>/details/',
         ArtistDetailView.as_view(), name='artist_details'),
    path('artists/<int:pk>/edit/', ArtistUpdateView.as_view(), name='artist_edit'),

    # collector urls
    path('collectors/all/', CollectorListView.as_view(), name='collector_list'),
    path('collectors/<int:pk>/details/', CollectorDetailView.as_view(),name='collector_details'),
    path('collectors/<int:pk>/edit/', CollectorUpdateView.as_view(), name='collector_edit'),

    # event urls
    path('events/all/', EventListView.as_view(), name="event_list"),
    path('events/add/', EventCreateView.as_view(),name="event_create"),
    path('events/<int:pk>/details/', EventDetailView.as_view(),name="event_details"),
    path('events/<int:pk>/edit/', EventUpdateView.as_view(),name="event_edit"),
]
