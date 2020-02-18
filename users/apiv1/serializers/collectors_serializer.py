from rest_framework.serializers import ModelSerializer
from users.models import CollectorProfile

class CollectorProfileSerializer(ModelSerializer):
     class Meta:
         model = CollectorProfile
         fields = '__all__'