from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import CollectorProfile
from django.contrib.auth import get_user_model

User = get_user_model()


class CollectorProfileUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number', 'email')


class CollectorProfileSerializer(ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CollectorProfile
        fields = '__all__'


class CollectorProfileDetailSerializer(ModelSerializer):
    user = CollectorProfileUserSerializer()

    class Meta:
        model = CollectorProfile
        fields = ('id', 'bio', 'user', 'county', 'birth_place',
                  'photo', 'created_on', 'updated_on')
