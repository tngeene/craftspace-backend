from django.contrib.auth import get_user_model
from rest_framework import serializers

from ...models import CustomOrder

User = get_user_model()

class CustomOrderCreateSerializer(serializers.ModelSerializer):
    requested_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CustomOrder
        fields = '__all__'

class CustomOrderUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name')

class CustomOrderDetailSerializer(serializers.ModelSerializer):
    requested_by = CustomOrderUsersSerializer()
    artist = CustomOrderUsersSerializer()
    medium = serializers.StringRelatedField()

    class Meta:
        model = CustomOrder
        fields = ('id','description','picture','size','medium','due_date','artist',
            'requested_by','phone_number','email','created_on','updated_on',)
