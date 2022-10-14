from django.contrib import admin

# Register your models here.


from .models import Territory, TerritoryName, TerritoryGroup, Language


class CountryAdmin(admin.ModelAdmin):
    pass


class CountryNameAdmin(admin.ModelAdmin):
    pass


class ContinentAdmin(admin.ModelAdmin):
    pass


class LanguageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Territory, CountryAdmin)
admin.site.register(TerritoryName, CountryNameAdmin)
admin.site.register(TerritoryGroup, ContinentAdmin)
admin.site.register(Language, LanguageAdmin)
