from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import ArtistProfile

class ArtistProfileSerializer(ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
     model = ArtistProfile
     fields = '__all__'