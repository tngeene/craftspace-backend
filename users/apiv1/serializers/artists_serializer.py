from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import ArtistProfile, Rating
from django.db.models import Avg, Sum
from django.contrib.auth import get_user_model

User = get_user_model()


class ArtistRatingSerializer(ModelSerializer):
    posted_by = serializers.StringRelatedField()

    class Meta:
        model = Rating
        fields = ('id', 'rating', 'comment', 'posted_by',
                  'created_at', 'updated_on')


class ArtistProfileCreateSerializer(ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = ArtistProfile
        fields = '__all__'


class ArtistProfileUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'phone_number', 'email')


class ArtistProfileListSerializer(ModelSerializer):
    user = ArtistProfileUserSerializer()
    average_rating = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()

    class Meta:
        model = ArtistProfile
        fields = ('id', 'bio', 'user', 'county', 'birth_place',
                  'photo', 'ratings', 'average_rating', 'created_on', 'updated_on')

    def get_average_rating(self, obj):
        avg_rating = obj.ratings.all().aggregate(Avg('rating'))
        return avg_rating['rating__avg']

    def get_ratings(self, obj):
        total_ratings = obj.ratings.all().count()
        return total_ratings


class ArtistProfileDetailSerializer(ModelSerializer):
    user = ArtistProfileUserSerializer()
    ratings = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = ArtistProfile
        fields = ('id', 'bio', 'user', 'county',
                  'birth_place', 'photo', 'ratings', 'average_rating')

    def get_average_rating(self, obj):
        avg_rating = obj.ratings.all().aggregate(Avg('rating'))
        return avg_rating['rating__avg']

    def get_ratings(self, obj):
        total_ratings = obj.ratings.all().count()
        return total_ratings
