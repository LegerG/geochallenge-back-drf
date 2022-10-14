import uuid
from django.db import models


class GeographyBase(models.Model):
    code = models.CharField(help_text="Identifying code based on ISO 3166-1 alpha-2 code for countries",
                            max_length=6, primary_key=True)
    wikipedia_link = models.URLField(
        max_length=150, help_text="Link to the Wikipedia page", blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.code


class Territory(GeographyBase):
    """
    A country in the world, principally identified by its ISO 3166-1 alpha-2 code.
    """
    groups = models.ManyToManyField(help_text="The groups that this territory belongs to (e.g. Continent, Geographical area, Political organization, etc.)",
                                    to='TerritoryGroup', related_name='territories')


class TerritoryGroup(GeographyBase):
    """
    A group of territory in the world. By example, the European Union is a group of countries or the Asian continent.
    """
    CONTINENT = 'CON'
    AREA = 'ARE'
    COUNTRY = 'CTR'
    POLITICAL = 'POL'
    OTHER = 'OTH'

    TERRITORY_GROUP_TYPOLOGY = (
        (CONTINENT, 'Continent'),
        (AREA, 'Area'),
        (COUNTRY, 'Country'),
        (POLITICAL, 'Political'),
        (OTHER, 'Other'),
    )

    typology = models.CharField(help_text="Typology of a territory group (e.g. Continent, Geographical area, Political organization, etc.)",
                                max_length=3, choices=TERRITORY_GROUP_TYPOLOGY, default=CONTINENT)


class Language(models.Model):
    """
    A supported language in the application, principally identified by its ISO 639-1 code.
    """
    code = models.CharField(help_text="ISO 639-1 code",
                            max_length=6, primary_key=True)
    name = models.CharField(help_text="Language name in the language itself",
                            max_length=150, unique=True)

    def __str__(self):
        return self.code


class TerritoryName(models.Model):
    """
    A name for a country in a particular language.

    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    territory = models.ForeignKey(help_text="Territory reference",
                                  to=Territory, on_delete=models.CASCADE, related_name="territoryname_set")
    language = models.ForeignKey(help_text="Language reference",
                                 to=Language, on_delete=models.CASCADE, related_name="territoryname_set")
    name = models.CharField(help_text="Territory name in the language",
                            max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['territory', 'language'], name='unique_territory_language')
        ]
        indexes = [
            models.Index(fields=['territory', 'language'],
                         name='territory_language_idx')
        ]

    def __str__(self):
        return "%s (%s)" % (self.name, self.language.code)
