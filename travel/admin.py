from django.contrib import admin
from .models import Destination, Checkoff, Next


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    fields = (('city', 'country'), 'adventure', 'climate', 'flight', 'image')
    list_display = (('city', 'country'))
    list_filter = ('city', 'adventure', 'climate', 'flight')
    ordering = ('city',)


@admin.register(Checkoff)
class CheckoffAdmin(admin.ModelAdmin):
    fields = (('city', 'country'), 'adventure', 'climate', 'flight', 'image')
    list_display = (('city', 'country'))
    ordering = ('city',)
    

@admin.register(Next)
class CheckoffAdmin(admin.ModelAdmin):
    fields = ('adventure', 'climate', 'flight')

