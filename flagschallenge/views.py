from rest_framework import generics

from flagschallenge.serialisers import GeographySerializer, TerritoryNameSerializer
from .models import Territory, TerritoryName, Language, TerritoryGroup
from rest_framework.exceptions import NotFound


class TerritoryView(generics.ListAPIView):
    serializer_class = GeographySerializer

    def get_queryset(self):
        group_code = self.request.query_params.get('group', '').lower()
        size = int(self.request.query_params.get('size', -1))

        if group_code != '' and not TerritoryGroup.objects.filter(code=group_code).exists():
            raise NotFound("Territory group not found")

        queryset = Territory.objects.all()
        queryset = queryset.order_by('?')  # Always random order

        if group_code != '':
            queryset = queryset.filter(groups__code=group_code)

        if size > 0:
            queryset = queryset[:size]

        return queryset


class TerritoryNameView(generics.ListAPIView):
    serializer_class = TerritoryNameSerializer

    def get_queryset(self):
        lang_code = self.request.query_params.get('lang', 'en').lower()
        group_code = self.request.query_params.get('group', '').lower()

        if lang_code != '' and not Language.objects.filter(code=lang_code).exists():
            raise NotFound("Language not found")

        if group_code != '' and not TerritoryGroup.objects.filter(code=group_code).exists():
            raise NotFound("Territory group not found")

        queryset = TerritoryName.objects.all().filter(language__code=lang_code)

        if group_code != '':
            queryset = queryset.filter(territory__groups__code=group_code)

        return queryset

class TerritoryGroupView(generics.ListAPIView):
    serializer_class = GeographySerializer
    queryset = TerritoryGroup.objects.all()