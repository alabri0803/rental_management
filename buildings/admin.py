from django.contrib import admin
from .models import Governorate, Wilayat, Building, Floor, Unit

@admin.register(Governorate)
class GovernorateAdmin(admin.ModelAdmin):
  list_display = ('name', 'code')
  search_fields = ('name', 'code')

@admin.register(Wilayat)
class WilayatAdmin(admin.ModelAdmin):
  list_display = ('name', 'governorate', 'code')
  list_filter = ('governorate',)
  search_fields = ('name', 'code')

class FloorInline(admin.TabularInline):
  model = Floor
  extra = 1

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
  list_display = ('name', 'building_type', 'governorate', 'wilayat')
  list_filter = ('building_type', 'governorate', 'wilayat')
  search_fields = ('name', 'address')
  inlines = [FloorInline]

class UnitInline(admin.TabularInline):
  model = Unit
  extra = 1

@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
  list_display = ('building', 'number')
  list_filter = ('building',)
  inlines = [UnitInline]

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
  list_display = ('unit_number', 'unit_type', 'floor', 'area', 'is_available')
  list_filter = ('unit_type', 'is_available', 'floor__building')
  search_fields = ('unit_number',)
  list_editable = ('is_available',)