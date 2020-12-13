from core.apiv1.views.events import (EventCreateAPIView, EventListAPIView,
                                     EventRetrieveUpdateDestroyAPIView)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.feedback import (FeedbackListCreateApiView,
                             FeedbackRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('events/', EventListAPIView.as_view()),
    path('events/add/', EventCreateAPIView.as_view()),
    path('events/<int:pk>/', EventRetrieveUpdateDestroyAPIView.as_view()),

    path('feedback/', FeedbackListCreateApiView.as_view()),
    path('feedback/<int:pk>/', FeedbackRetrieveUpdateDestroyAPIView.as_view())
]
