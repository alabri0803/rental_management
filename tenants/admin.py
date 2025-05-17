from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import Tenant


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
  class Media:
    css = {
      'all': ('css/admin_rtl.css',)
    }
  list_display = ('full_name', 'national_id', 'phone', 'status_display', 'show_photo_id')
  list_filter = ('status',)
  search_fields = ('full_name', 'national_id', 'phone')
  ordering = ('full_name',)

  def status_display(self, obj):
    status_color = {
      'AC': 'green',
      'LE': 'gray',
      'LT': 'orange',
    }
    color = status_color.get(obj.status, 'black')
    return format_html('<span style="color: {};">{}</span>', color, obj.get_status_display())
  status_display.short_description = _('الحالة')

  def show_photo_id(self, obj):
    if obj.photo_id:
      return format_html('<img src="{}" width="50" height="50" style="border-radius:5px;" />', obj.photo_id.url)
    return "-"
  show_photo_id.short_description = "صورة الهوية"