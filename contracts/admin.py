from django.contrib import admin
from django.utils.html import format_html

from .models import Contract, ContractCancellation, Document, Payment, UtilityCommitment


class PaymentInline(admin.TabularInline):
  """إدارة المدفوعات داخل صفحة العقد"""
  model = Payment
  extra = 1
  readonly_fields = ('created_at', 'updated_at')

class DocumentInline(admin.TabularInline):
  """إدارة المستندات داخل صفحة العقد"""
  model = Document
  extra = 0
  readonly_fields = ('created_at', 'updated_at')

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
  """إدارة العقود"""
  list_display = ('contract_number', 'property', 'owner', 'tenant', 'monthly_rent', 'status_colored', 'start_date', 'end_date')
  list_filter = ('status', 'start_date', 'end_date', 'created_at')
  search_fields = ('contract_number', 'property__title', 'owner__user__first_name', 'tenant__user__first_name')
  readonly_fields = ('created_at', 'updated_at', 'signed_at')
  inlines = [PaymentInline, DocumentInline]
  fieldsets = (
    ('أطراف العقد', {
      'fields': ('property', 'owner', 'tenant')
    }),
    ('تفاصيل العقد', {
      'fields': ('contract_number', 'start_date', 'end_date', 'status')
    }),
    ('المبالغ المالية', {
      'fields': ('monthly_rent', 'security_deposit')
    }),
    ('الرسوم', {
      'fields': ('admin_fees', 'office_fees', 'additional_fees', 'total_fees')
    }),
    ('الشروط', {
      'fields': ('terms_and_conditions', 'notes')
    }),
    ('التواريخ', {
      'fields': ('created_at', 'updated_at', 'signed_at'),
      'classes': ('collapse',)
    }),
  )
  def status_colored(self, obj):
    """عرض حالة العقد بالألوان"""
    color = obj.get_status_color()
    return format_html('<span style="color: {}; font-weght: bold;">{}</span>', color, obj.get_status_display())
  status_colored.short_description = 'حالة العقد'
  def get_queryset(self, request):
    return super().get_queryset(request).select_related('property', 'owner__user', 'tenant__user')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
  """إدارة المدفوعات"""
  list_display = ('contract', 'payment_type', 'amount', 'due_date', 'status', 'paid_date')
  list_filter = ('payment_type', 'status', 'due_date', 'paid_date')
  search_fields = ('contract__contract_number', 'contract__property__title')
  readonly_fields = ('created_at', 'updated_at')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
  """إدارة المستندات"""
  list_display = ('title', 'contract', 'document_type', 'created_at')
  list_filter = ('document_type', 'created_at')
  search_fields = ('title', 'contract__contract_number')
  readonly_fields = ('created_at', 'updated_at')

@admin.register(ContractCancellation)
class ContractCancellationAdmin(admin.ModelAdmin):
  """إدارة إلغاء العقود"""
  list_display = ('contract', 'cancellation_date', 'owner_signature', 'tenant_signature')
  search_fields = ('contract__contract_number', 'reason')
  readonly_fields = ('created_at',)

@admin.register(UtilityCommitment)
class UtilityCommitmentAdmin(admin.ModelAdmin):
  """إدارة تعهدات سداد المرافق"""
  list_display = ('contract', 'electricity_commitment', 'water_commitment', 'tenant_signature', 'signature_date')
  list_filter = ('electricity_commitment', 'water_commitment', 'tenant_signature')
  search_fields = ('contract__contract_number',)
  readonly_fields = ('created_at',)