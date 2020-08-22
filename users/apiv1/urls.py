from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.apiv1.views.artists import (ArtistProfileCreateAPIView,
                                       ArtistProfileDetailView,
                                       ArtistProfileListAPIView,
                                       ArtistProfileUpdateAPIView)
from users.apiv1.views.collectors import CollectorProfileApiView
from users.apiv1.views.users import ArtistListAPIView, CollectorListAPIView

router = DefaultRouter()
# router.register('artists/profile',ArtistProfileApiView,basename='artist_profile')
router.register('collectors/profile',CollectorProfileApiView,basename='collector_profile')
urlpatterns = [
    path('artists/', ArtistListAPIView.as_view()),
    path('artists/profile/add', ArtistProfileCreateAPIView.as_view()),
    path('artists/profiles/', ArtistProfileListAPIView.as_view()),
    path('artists/profile/<int:pk>/',ArtistProfileUpdateAPIView.as_view()),
    path('artists/profile/<int:pk>/details',ArtistProfileDetailView.as_view()),
    path('collectors/', CollectorListAPIView.as_view()),
    path('',include(router.urls)),
]
