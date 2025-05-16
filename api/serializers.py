from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from tenants.models import Tenant
from contracts.models import Contract
from payments.models import Payment
from buildings.models import Unit

class TenantSerializer(serializers.ModelSerializer):
  status_display = serializers.CharField(source='get_status_display', read_only=True)
  class Meta:
    model = Tenant
    fields = [
      'id',
      'full_name',
      'national_id',
      'phone',
      'email',
      'address',
      'status',
      'status_display',
      'photo_id',
    ]
    extra_kwargs = {
      'full_name': {'label': _('الاسم الكامل')},
      'national_id': {'label': _('الرقم الوطني')},
      'phone': {'label': _('رقم الهاتف')},
      'email': {'label': _('البريد الإلكتروني')},
      'address': {'label': _('العنوان')},
      'status': {'label': _('الحالة')},
      'photo_id': {'label': _('صورة الهوية')}
    }

class UnitSerializer(serializers.ModelSerializer):
  type_display = serializers.CharField(source='get_type_display', read_only=True)
  class Meta:
    model = Unit
    fields = [
      'id',
      'name',
      'building_name',
      'floor',
      'type',
      'type_display',
      'is_occupied',
      'is_furnished',
      'area',
      'coordinates',
    ]
    extra_kwargs = {
      'name': {'label': _('اسم الوحدة')},
      'building_name': {'label': _('اسم البناية')},
      'floor': {'label': _('الطابق')},
      'type': {'label': _('نوع الوحدة')},
      'is_occupied': {'label': _('مشغولة؟')},
      'is_furnished': {'label': _('مؤثثة؟')},
      'area': {'label': _('المساحة بالمتر')},
      'coordinates': {'label': _('الإحداثيات')}
    }
    
class ContractReadSerializer(serializers.ModelSerializer):
  tenant = TenantSerializer(read_only=True)
  unit = UnitSerializer(read_only=True)
  status_display = serializers.CharField(source='get_status_display', read_only=True)
  
  class Meta:
    model = Contract
    fields = [
      'id',
      'contract_number',
      'tenant',
      'unit',
      'start_date',
      'end_date',
      'rent_amount',
      'status',
      'status_display',
      'contract_file',
    ]

class ContractWriteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contract
    fields = '__all__'
    extra_kwargs = {
      'contract_number': {'label': _('رقم العقد')},
      'tenant': {'label': _('المستأجر')},
      'unit': {'label': _('الوحدة')},
      'start_date': {'label': _('تاريخ البداية')},
      'end_date': {'label': _('تاريخ النهاية')},
      'rent_amount': {'label': _('الايجار الشهري')},
      'status': {'label': _('الحالة')},
      'contract_file': {'label': _('ملف العقد')}
    }

class PaymentReadSerializer(serializers.ModelSerializer):
  contract = ContractReadSerializer(read_only=True)
  method_display = serializers.CharField(source='get_method_display', read_only=True)
  amount_riyal = serializers.SerializerMethodField()

  def get_amount_riyal(self, obj):
    return f"{obj.amount:3f} ر.ع"
  
  class Meta:
    model = Payment
    fields = [
      'id',
      'contract',
      'amount',
      'amount_riyal',
      'date',
      'method',
      'method_display',
      'receipt'
    ]

class PaymentWriteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Payment
    fields = '__all__'
    extra_kwargs = {
      'contract': {'label': _('العقد')},
      'amount': {'label': _('المبلغ')},
      'date': {'label': _('تاريخ الدفع')},
      'method': {'label': _('طريقة الدفع')},
      'receipt': {'label': _('إيصال الدفع')}
    }