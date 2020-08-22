from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import ArtistProfile, Rating
from django.db.models import Avg


class ArtistRatingSerializer(ModelSerializer):
    posted_by = serializers.StringRelatedField()

    class Meta:
        model = Rating
        fields = ('id','rating','comment', 'posted_by', 'created_at', 'updated_on')


class ArtistProfileCreateSerializer(ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = ArtistProfile
        fields = '__all__'


class ArtistProfileListSerializer(ModelSerializer):
    user = serializers.StringRelatedField()
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = ArtistProfile
        fields = ('id', 'bio', 'user', 'county','birth_place',
                'photo', 'average_rating','created_on', 'updated_on')

    def get_average_rating(self, obj):
        avg_rating = obj.ratings.all().aggregate(Avg('rating'))
        return avg_rating['rating__avg']

class ArtistProfileDetailSerializer(ModelSerializer):
    user = serializers.StringRelatedField()
    ratings = ArtistRatingSerializer(many=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = ArtistProfile
        fields = ('id', 'bio', 'user', 'county',
                  'birth_place', 'photo', 'ratings','average_rating')

    def get_average_rating(self, obj):
        avg_rating = obj.ratings.all().aggregate(Avg('rating'))
        return avg_rating['rating__avg']
