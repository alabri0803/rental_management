from django.contrib import admin
from .models import Building, Unit

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
  list_display = ('name', 'building_type', 'address')

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
  list_display = ('building', 'unit_type', 'floor', 'number', 'is_available')