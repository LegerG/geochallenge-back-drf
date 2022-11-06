from rest_framework import serializers
from .models import Territory, TerritoryName, TerritoryGroup


class GeographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Territory
        fields = ('code', 'wikipedia_link')


class TerritoryNameSerializer(serializers.ModelSerializer):
    code = serializers.CharField(source='territory')

    class Meta:
        model = TerritoryName
        fields = ('name', 'code')
