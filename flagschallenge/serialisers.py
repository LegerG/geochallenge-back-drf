from rest_framework import serializers
from .models import Territory, TerritoryName


class TerritorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Territory
        fields = ('code', 'wikipedia_link')


class TerritoryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TerritoryName
        fields = ('name',)
