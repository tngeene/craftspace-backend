from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apiv1.views.events import EventListAPIView, EventCreateAPIView, EventRetrieveUpdateDestroyAPIView



urlpatterns = [
    path('events/',EventListAPIView.as_view()),
    path('events/add/', EventCreateAPIView.as_view()),
    path('events/<int:pk>/', EventRetrieveUpdateDestroyAPIView.as_view())
]
