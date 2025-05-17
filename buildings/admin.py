from django.contrib import admin
from .models import Unit
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
  list_display = ('name', 'building_name', 'floor', 'get_type', 'is_occupied_display', 'area')
  list_filter = ('type', 'is_occupied')
  search_fields = ('name', 'building_name')

  def get_type(self, obj):
    return obj.get_type_display()
  get_type.short_description = _('نوع الوحدة')

  def is_occupied_display(self, obj):
    color = 'green' if obj.is_occupied else 'gray'
    text = _('مشغولة') if obj.is_occupied else _('شاغرة')
    return format_html('<span style="color: {};">{}</span>', color, text)
  is_occupied_display.short_description = _('الحالة')