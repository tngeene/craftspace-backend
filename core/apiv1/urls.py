from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apiv1.views.events import EventsApiView

router = DefaultRouter()
router.register('events',EventsApiView,base_name='events')

urlpatterns = [
    path('',include(router.urls)),
]
