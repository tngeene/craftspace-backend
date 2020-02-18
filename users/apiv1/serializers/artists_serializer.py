from rest_framework.serializers import ModelSerializer
from users.models import ArtistProfile

class ArtistProfileSerializer(ModelSerializer):
     class Meta:
         model = ArtistProfile
         fields = '__all__'