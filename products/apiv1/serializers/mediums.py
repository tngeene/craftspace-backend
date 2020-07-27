from rest_framework import serializers

from ...models import Medium

class MediumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medium
        fields = ('__all__')