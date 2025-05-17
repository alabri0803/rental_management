from django.contrib import admin
from .models import Payment
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
  list_display = ('contract', 'amount_omr', 'date', 'method_display', 'show_receipt')
  list_filter = ('method', 'date')
  search_fields = ('contract__contract_number', 'contract__tenant__full_name')
  date_hierarchy = 'date'

  def amount_omr(self, obj):
    return f"{obj.amount:.3f} ر.ع"
  amount_omr.short_description = _('المبلغ')

  def method_display(self, obj):
    return obj.get_method_display()
  method_display.short_description = _('طريقة الدفع')

  def show_receipt(self, obj):
    if obj.receipt:
      return format_html('<a href="{}" target="_blank">{}</a>', obj.receipt.url, _("عرض الإيصال"))
    return "-"
  show_receipt.short_description = _("الإيصال")