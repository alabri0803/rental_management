from rest_framework import viewsets
from .serializers import TenantSerializer
from tenants.models import Tenant

class TenantViewSet(viewsets.ModelViewSet):
  queryset = Tenant.objects.all()
  serializer_class = TenantSerializer