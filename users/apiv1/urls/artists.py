from django.urls import path

from ..views.artists import (ArtistListAPIView, ArtistProfileCreateAPIView,
                             ArtistProfileRetrieveUpdateDestroyAPIView,
                             RatingPostAPIView)

app_name = "artists"

urlpatterns = [
    path('', ArtistListAPIView.as_view(), name="artist_list"),
    path('profiles/', ArtistProfileCreateAPIView.as_view(),name="artist_profile_list_create"),
    path('profiles/<int:pk>/', ArtistProfileRetrieveUpdateDestroyAPIView.as_view(),name="artist_profile_rud"),
    path('profiles/post-rating/', RatingPostAPIView.as_view(), name='post_rating'),
]
