from django.core.exceptions import ObjectDoesNotExist
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from core.apiv1.serializers.events_serializer import EventSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from users.models import UserAccount

from ..serializers.artists_serializer import ArtistProfileListSerializer
from ..serializers.collectors_serializer import CollectorProfileSerializer


class UserRegistrationSerializer(UserCreateSerializer):
    """
    Overrides djoser registration behavior to accept membership type on sign up
    """
    phone_number = PhoneNumberField()
    class Meta(UserCreateSerializer.Meta):
        fields = ('id','email','first_name','last_name','phone_number','membership_type','password',)

class CustomUserSerializer(UserSerializer):
    # artist_profile = ArtistProfileSerializer(read_only=True)
    # collector_profile = CollectorProfileSerializer(read_only=True)
    has_profile = serializers.SerializerMethodField()

    """
    override djoser's user serializer to reflect AbstractUser fields
    """
    class Meta(UserSerializer.Meta):
        fields = ('id','email','first_name','last_name','phone_number','membership_type','is_active','has_profile')

    def get_has_profile(self, obj):
        if obj.membership_type == 'Artist':
            # check if the users have profiles associated with them
            try:
                return bool(obj.artist_profile)
            except ObjectDoesNotExist:
                return False

        elif obj.membership_type == 'Collector':
            try:
                return bool(obj.collector_profile)
            except ObjectDoesNotExist:
                return False
        else:
            return None

class UserAccountSerializer(serializers.ModelSerializer):
    artist_profile = ArtistProfileListSerializer(read_only=True)
    events = EventSerializer(many=True, read_only=True)
    class Meta:
        fields = (
            'id',
            'email',
            'phone_number',
            'membership_type',
            'first_name',
            'last_name',
            'is_active',
            'artist_profile',
            'events'
        )
        model = UserAccount

        def get_has_profile(self, obj):
            if obj.membership_type == 'Artist':
            # check if the users have profiles associated with them
                try:
                    return bool(obj.member_profiles)
                except ObjectDoesNotExist:
                    return False

            elif obj.membership_type == 'Collector':
                try:
                    return bool(obj.trainer_profiles)
                except ObjectDoesNotExist:
                    return False
            else:
                return None
