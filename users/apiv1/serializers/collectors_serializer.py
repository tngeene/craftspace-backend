from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import CollectorProfile


class CollectorProfileSerializer(ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CollectorProfile
        fields = '__all__'