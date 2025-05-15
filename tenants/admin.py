from django.contrib import admin
from .models import Tenant
from django.utils.html import format_html

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
  list_display = ('full_name', 'phone', 'status', 'show_photo_id')
  list_filter = ('status',)
  search_fields = ('full_name', 'national_id', 'phone')

  def show_photo_id(self, obj):
    if obj.photo_id:
      return format_html('<img src="{}" width="50" height="50" style="border-radius:5px;" />', obj.photo_id.url)
    return "-"
  show_photo_id.short_description = "صورة الهوية"