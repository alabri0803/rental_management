from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from tenants.models import Tenant
from contracts.models import Contract
from payments.models import Payment
from buildings.models import Unit
from .serializers import TenantSerializer, ContractReadSerializer, ContractWriteSerializer, PaymentReadSerializer, PaymentWriteSerializer, UnitSerializer

class TenantViewSet(viewsets.ModelViewSet):
  queryset = Tenant.objects.all()
  serializer_class = TenantSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
  filter_backends = [SearchFilter, OrderingFilter]
  search_fields = ['full_name', 'national_id', 'phone']
  ordering_fields = ['full_name', 'status']

class UnitViewSet(viewsets.ModelViewSet):
  queryset = Unit.objects.all()
  serializer_class = UnitSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
  filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
  filterset_fields = ['type', 'is_occupied']
  search_fields = ['name', 'building_name']
  ordering_fields = ['floor', 'area']
  
class ContractViewSet(viewsets.ModelViewSet):
  queryset = Contract.objects.select_related('tenant', 'unit').all()
  permission_classes = [IsAuthenticatedOrReadOnly]
  filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
  filterset_fields = ['status', 'unit__type']
  search_fields = ['contract_number', 'tenant__full_name']
  ordering_fields = ['start_date', 'end_date', 'rent_amount']

  def get_serializer_class(self):
    if self.request.method in ['GET']:
      return ContractReadSerializer
    return ContractWriteSerializer
  
class PaymentViewSet(viewsets.ModelViewSet):
  queryset = Payment.objects.select_related('contract').all()
  permission_classes = [IsAuthenticatedOrReadOnly]
  filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
  filterset_fields = ['method', 'contract__status']
  search_fields = ['contract__contract_number']
  ordering_fields = ['date', 'amount']

  def get_serializer_class(self):
    if self.request.method in ['GET']:
      return PaymentReadSerializer
    return PaymentWriteSerializer