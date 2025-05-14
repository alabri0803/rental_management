from rest_framework import viewsets
from tenants.models import Tenant
from contracts.models import Contract
from payments.models import Payment
from buildings.models import Unit
from .serializers import TenantSerializer, ContractSerializer, PaymentSerializer, UnitSerializer

class TenantViewSet(viewsets.ModelViewSet):
  queryset = Tenant.objects.all()
  serializer_class = TenantSerializer

class ContractViewSet(viewsets.ModelViewSet):
  queryset = Contract.objects.all()
  serializer_class = ContractSerializer

class PaymentViewSet(viewsets.ModelViewSet):
  queryset = Payment.objects.all()
  serializer_class = PaymentSerializer

class UnitViewSet(viewsets.ModelViewSet):
  queryset = Unit.objects.all()
  serializer_class = UnitSerializer