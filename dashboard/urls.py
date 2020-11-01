from django.urls import path

from dashboard.views.dashboard import DashboardTemplateView

# artists views
from .views.artists import ArtistDetailView, ArtistListView, ArtistUpdateView
from .views.collectors import CollectorDetailView, CollectorListView, CollectorUpdateView
from .views.admin_actions import activate_user, suspend_user, UserConfirmSuspendView
app_name = 'dashboard'

urlpatterns = [
    path('', DashboardTemplateView.as_view(), name='index'),

    # admin action urls
    path('users/<int:pk>/confirm-suspend/', UserConfirmSuspendView.as_view(), name="user_confirm_suspend"),
    path('users/<int:pk>/suspend_user/', suspend_user,name="user_suspend_action"),
    path('users/<int:pk>/unsuspend_user/', activate_user,name="user_unsuspend_action"),

    # artist urls
    path('artists/all/', ArtistListView.as_view(), name='artist_list'),
    path('artists/<int:pk>/details/',
         ArtistDetailView.as_view(), name='artist_details'),
    path('artists/<int:pk>/edit/', ArtistUpdateView.as_view(), name='artist_edit'),

    # collector urls
    path('collectors/all/', CollectorListView.as_view(), name='collector_list'),
    path('collectors/<int:pk>/details/', CollectorDetailView.as_view(),name='collector_details'),
    path('collectors/<int:pk>/edit/', CollectorUpdateView.as_view(), name='collector_edit'),
]
