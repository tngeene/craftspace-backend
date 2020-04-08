from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.apiv1.views.users import ArtistListAPIView, CollectorListAPIView
from users.apiv1.views.artists import ArtistProfileApiView, ArtistProfileCreateAPIView, ArtistProfileUpdateAPIView, ArtistProfileListAPIView
from users.apiv1.views.collectors import CollectorProfileApiView

router = DefaultRouter()
# router.register('artists/profile',ArtistProfileApiView,basename='artist_profile')
router.register('collectors/profile',CollectorProfileApiView,basename='collector_profile')
urlpatterns = [
    path('artists/', ArtistListAPIView.as_view()),
    path('artists/profile/add', ArtistProfileCreateAPIView.as_view()),
    path('artists/profiles', ArtistProfileListAPIView.as_view()),
    path('artists/profile/<int:pk>/edit',ArtistProfileUpdateAPIView.as_view()),
    path('collectors/', CollectorListAPIView.as_view()),
    path('',include(router.urls)),
]
