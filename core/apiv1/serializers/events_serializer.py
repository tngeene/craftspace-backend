from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.models import Event

class EventSerializer(ModelSerializer):
    uploaded_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Event
        fields = "__all__"