from django.contrib import admin
from .models import Choice, Question, Kayttajat, Toimipiste, Palaute

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

class ToimipisteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Toimipisteen nimi',               {'fields': ['toimipiste_nimi']}),
        ('Pvm tiedot', {'fields': ['last_update'], 'classes': ['collapse']}),
        ('Osoitteen tiedot', {'fields': ['osoite_id']})
    ]
    list_display = ('toimipiste_nimi', 'last_update')
    list_filter = ['last_update']
    search_fields = ['toimipiste_nimi']

admin.site.register(Toimipiste, ToimipisteAdmin)


class PalauteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Toimipiste, jota palaute koskee', {'fields': ['toimipiste_id']}),
        (None, {'fields': ['palaute_pvm'], 'classes': ['collapse']}),
        (None, {'fields': ['arvosana']}),
        ('Hyvää', {'fields': ['hyvaa']}),
        (None, {'fields': ['huonoa']}),
        (None, {'fields': ['parannettavaa']}),
    ]
    list_display = ('toimipiste_id', 'palaute_pvm')
    list_filter = ['toimipiste_id']
    search_fields = ['toimipiste_id']

admin.site.register(Palaute, PalauteAdmin)
    