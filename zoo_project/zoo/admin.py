from django.contrib import admin
from .models import Animal

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'health')
    list_filter = ('health',)
    search_fields = ('name', 'species')

admin.site.register(Animal, AnimalAdmin)