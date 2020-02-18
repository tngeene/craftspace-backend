from djoser.serializers import UserCreateSerializer,UserSerializer
from rest_framework import serializers

from users.models import UserAccount

class UserRegistrationSerializer(UserCreateSerializer):
    """
    Overrides djoser registration behavior to accept membership type on sign up
    """
    class Meta(UserCreateSerializer.Meta):
        fields = ('email','first_name','last_name','phone_number','password','membership-type',)

class CustomUserSerializer(UserSerializer):
    """
    override djoser's user serializer to reflect AbstractUser fields
    """
    class Meta(UserSerializer.Meta):
        fields = ('email','first_name','last_name','phone_number','membership_type',)


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'email',
            'phone_number',
            'membership_type',
            'first_name',
            'last_name',
            'is_active',
        )
        model = UserAccount
