from django.contrib import admin
from .models import Contract

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
  list_display = ('contract_number', 'tenant', 'unit', 'start_date', 'end_date', 'rent_amount')
  list_filter = ('purpose_of_contract', 'land_usage_puropose', 'residential_usage')
  search_fields = ('contract_number', 'lessor_name', 'tenant__full_name')