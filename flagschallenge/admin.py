from django.contrib import admin

# Register your models here.


from .models import Territory, TerritoryName, TerritoryGroup, Language, GeographyBase


class GeographyBaseAdmin(admin.ModelAdmin):
    pass

class TerritoryAdmin(admin.ModelAdmin):
    pass


class TerritoryNameAdmin(admin.ModelAdmin):
    pass


class ContinentAdmin(admin.ModelAdmin):
    pass


class LanguageAdmin(admin.ModelAdmin):
    pass


admin.site.register(GeographyBase, GeographyBaseAdmin)
admin.site.register(Territory, TerritoryAdmin)
admin.site.register(TerritoryName, TerritoryNameAdmin)
admin.site.register(TerritoryGroup, ContinentAdmin)
admin.site.register(Language, LanguageAdmin)
