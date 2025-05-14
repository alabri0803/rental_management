from rest_framework import serializers
from tenants.models import Tenant
from contracts.models import Contract
from payments.models import Payment
from buildings.models import Unit

class TenantSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tenant
    fields = '__all__'

class ContractSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contract
    fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Payment
    fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):
  class Meta:
    model = Unit
    fields = '__all__'