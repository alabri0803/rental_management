from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
  list_display = ('contract', 'amount', 'date', 'method')
  list_filter = ('method', 'date')
  search_fields = ('contract__contract_number',)
  date_hierarchy = 'date'