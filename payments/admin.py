from django.contrib import admin
from .models import Payment
from django.utils.html import format_html

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
  list_display = ('contract', 'amount', 'date', 'method', 'show_receipt')
  list_filter = ('method', 'date')
  search_fields = ('contract__contract_number',)
  date_hierarchy = 'date'

  def show_receipt(self, obj):
    if obj.receipt:
      return format_html('<a href="{}" target="_blank">عرض الايصال</a>', obj.receipt.url)
    return "-"
  show_receipt.short_description = "إيصال الدفع"