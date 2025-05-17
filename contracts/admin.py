from django.contrib import admin
from .models import Contract
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
  list_display = ('contract_number', 'tenant', 'unit', 'start_date', 'end_date', 'colored_status')
  list_filter = ('status', 'start_date')
  search_fields = ('contract_number', 'tenant__full_name', 'unit__name')
  date_hierarchy = 'start_date'

  def colored_status(self, obj):
    color = {
      'AC': 'green',
      'EN': 'gray',
      'CA': 'red',
    }.get(obj.status, 'black')
    return format_html('<span style="color: {};">{}</span>', color, obj.get_status_display())
  colored_status.short_description = _('الحالة')