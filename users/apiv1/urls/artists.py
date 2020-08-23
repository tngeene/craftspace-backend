from django.urls import path

from ..views.artists import (ArtistProfileCreateAPIView, ArtistListAPIView,
                             ArtistProfileRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('', ArtistListAPIView.as_view(), name="artist_list"),
    path('profiles/', ArtistProfileCreateAPIView.as_view(),name="artist_profile_list_create"),
    path('profiles/<int:pk>/', ArtistProfileRetrieveUpdateDestroyAPIView.as_view(),name="artist_profile_rud")
]
