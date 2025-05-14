from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import Contract

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
  list_display = (
    'contract_number',
    'tenant_name',
    'unit_name',
    'start_date',
    'rent_amount_omr',
    'contract_duration',
    'months_left',
    #'registration_fee',
    'total_fees',
  )
  list_filter = (
    'start_date',
    'end_date',
  )
  search_fields = (
    'tenant__full_name',
    'unit__name',
    'activity',
  )
  readonly_fields = (
    'contract_number',
    'admin_fee',
    'office_fee',
    #'registration_fee',
    'total_fees',
    'contract_duration_months',
    'months_remaining',
  )
  def tenant_name(self, obj):
    return obj.tenant.full_name
  tenant_name.short_description = _("المستأجر")

  def unit_name(self, obj):
    return obj.unit.name
  unit_name.short_description = _("الوحدة")

  def rent_amount_omr(self, obj):
    return f"{obj.rent_amount:.3f} ر.ع"
  rent_amount_omr.short_description = _("الإيجار")

  def contract_duration(self, obj):
    return f"{obj.contract_duration_months} شهر"
  contract_duration.short_description = _("مدة العقد")

  def months_left(self, obj):
    remaining = obj.months_remaining
    color = "green" if remaining > 3 else "orange" if remaining > 0 else "red"
    return format_html('<span style="color:{};">{} شهر</span>', color, remaining)
  months_left.short_description = _("المتبقي")

  def colored_registration_fee(self, obj):
    formatted_fee = "{:.3f} ر.ع".format(float(obj.registration_fee))
    return format_html('<b style="color:blue;">{}</b>', formatted_fee)
  colored_registration_fee.short_description = _("رسوم التسجيل")


  def colored_total_fees(self, obj):
    pass
  colored_total_fees.short_description = _("إجمالي الرسوم")

  class Media:
    css = {
      'all': ('css/admin_rtl.css',)
    }