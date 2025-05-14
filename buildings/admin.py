from django.contrib import admin
from .models import Unit

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
  list_display = ('name', 'building_name', 'type', 'floor', 'is_occupied', 'is_furnished', 'area')
  list_filter = ('type', 'is_occupied', 'is_furnished')
  search_fields = ('name', 'building_name')
  ordering = ['building_name', 'floor']