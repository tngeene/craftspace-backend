from djoser.serializers import UserCreateSerializer,UserSerializer
from rest_framework import serializers
from ..serializers.artists_serializer import ArtistProfileSerializer
from ..serializers.collectors_serializer import CollectorProfileSerializer
from core.apiv1.serializers.events_serializer import EventSerializer

from users.models import UserAccount

class UserRegistrationSerializer(UserCreateSerializer):
    """
    Overrides djoser registration behavior to accept membership type on sign up
    """
    class Meta(UserCreateSerializer.Meta):
        fields = ('id','email','first_name','last_name','phone_number','membership_type','password',)

class CustomUserSerializer(UserSerializer):
    # artist_profile = ArtistProfileSerializer(read_only=True)
    collector_profile = CollectorProfileSerializer(read_only=True)
    my_events = EventSerializer(many=True, read_only=True)

    """
    override djoser's user serializer to reflect AbstractUser fields
    """
    class Meta(UserSerializer.Meta):
        fields = ('id','email','first_name','last_name','phone_number','membership_type', 'my_events', 'collector_profile')


class UserAccountSerializer(serializers.ModelSerializer):
    artist_profile = ArtistProfileSerializer(read_only=True)
    my_events = EventSerializer(many=True, read_only=True)
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
            'my_events'
        )
        model = UserAccount

