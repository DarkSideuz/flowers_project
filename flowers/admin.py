from django.contrib import admin

# Register your models here.

from .models import Type, Flower

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'description')
    list_filter = ('type',)
    search_fields = ('name', 'description')
