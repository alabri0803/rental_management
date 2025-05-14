from django.contrib import admin
from .models import Contract

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
  list_display = ('contract_number', 'tenant', 'unit', 'start_date', 'end_date', 'status')
  list_filter = ('status', 'start_date')
  search_fields = ('contract_number', 'tenant__full_name', 'unit__name')
  date_hierarchy = 'start_date'
  ordering = ['-start_date']