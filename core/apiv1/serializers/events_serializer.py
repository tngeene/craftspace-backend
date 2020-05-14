from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers
from core.models import Event
from django.forms import model_to_dict
from django.contrib.auth import get_user_model

class EventSerializer(ModelSerializer):
    # uploaded_by = serializers.StringRelatedField(read_only=True)
    uploaded_by = SerializerMethodField(read_only=True)
    class Meta:
        model = Event
        fields = "__all__"

    def get_uploaded_by(self, obj):
        owner = [model_to_dict(obj.uploaded_by,fields=['first_name','last_name','id'])]
        return owner
