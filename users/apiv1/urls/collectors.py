from django.urls import path

from ..views.collectors import (CollectorProfileListCreateAPIView,
                                CollectorProfileRUDAPIView,
                                CollectorsListAPIView)

app_name = "collectors"

urlpatterns = [
    path('', CollectorsListAPIView.as_view(),name="collectors_list"),
    path('profiles/', CollectorProfileListCreateAPIView.as_view(),name="collector_profile_list_create"),
    path('profiles/<int:pk>', CollectorProfileRUDAPIView.as_view(),name="collector_profile_rud_actions")
]
