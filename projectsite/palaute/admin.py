from django.contrib import admin
from .models import Toimipiste, Palaute, Osoite


class OsoiteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Katuosoite', {'fields': ['osoite']}),
        ('Postinumero', {'fields': ['postinumero']}),
        ('Kaupunki', {'fields': ['kaupunki']}),
        ('Pvm', {'fields': ['last_update'], 'classes': ['collapse']}),
    ]
    list_display = ['osoite']
    list_filter = ['last_update', 'kaupunki']
    search_fields = ['kaupunki']

admin.site.register(Osoite, OsoiteAdmin)


class ToimipisteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Toimipisteen nimi', {'fields': ['toimipiste_nimi']}),
        ('Pvm tiedot', {'fields': ['last_update'], 'classes': ['collapse']}),
        ('Osoitteen tiedot', {'fields': ['FK_osoite_id']}),
    ]
    list_display = ('toimipiste_nimi', 'FK_osoite_id')
    list_filter = ['last_update']
    search_fields = ['toimipiste_nimi']

admin.site.register(Toimipiste, ToimipisteAdmin)


class PalauteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Toimipiste, jota palaute koskee', {'fields': ['FK_toimipiste_id']}),
        (None, {'fields': ['palaute_pvm'], 'classes': ['collapse']}),
        (None, {'fields': ['arvosana']}),
        ('Hyvää', {'fields': ['hyvaa']}),
        (None, {'fields': ['huonoa']}),
        (None, {'fields': ['parannettavaa']})
    ]
    list_display = ('palaute_pvm', 'FK_toimipiste_id')
    list_filter = ['palaute_pvm', 'FK_toimipiste_id']
    search_fields = ['FK-toimipiste_id']

admin.site.register(Palaute, PalauteAdmin)
