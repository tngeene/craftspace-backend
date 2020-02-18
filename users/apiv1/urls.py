from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.apiv1.views.users import ArtistListAPIView, CollectorListAPIView
from users.apiv1.views.artists import ArtistProfileApiView
from users.apiv1.views.collectors import CollectorProfileApiView

router = DefaultRouter()
router.register('artists/profile',ArtistProfileApiView,base_name='artist_profile')
router.register('collectors/profile',CollectorProfileApiView,base_name='collector_profile')
urlpatterns = [
    path('artists/', ArtistListAPIView.as_view()),
    path('collectors/', CollectorListAPIView.as_view()),
    path('',include(router.urls)),
]
