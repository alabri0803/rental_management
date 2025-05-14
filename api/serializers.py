from rest_framework import serializers
from tenants.models import Tenant
from contracts.models import Contract
from payments.models import Payment
from buildings.models import Unit
from django.utils.translation import gettext_lazy as _
from datetime import date

class TenantSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tenant
    fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):
  type_display = serializers.CharField(source='get_type_display', read_only=True)
  class Meta:
    model = Unit
    fields = '__all__'
    
class ContractReadSerializer(serializers.ModelSerializer):
  tenant = TenantSerializer(read_only=True)
  unit = UnitSerializer(read_only=True)
  status_display = serializers.CharField(source='get_status_display', read_only=True)
  
  class Meta:
    model = Contract
    fields = '__all__'

class ContractWriteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contract
    fields = '__all__'

class PaymentReadSerializer(serializers.ModelSerializer):
  contract = ContractReadSerializer(read_only=True)
  method_display = serializers.CharField(source='get_method_display', read_only=True)
  
  class Meta:
    model = Payment
    fields = '__all__'

class PaymentWriteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Payment
    fields = '__all__'