from django.shortcuts import render
from contracts.models import Contract
from tenants.models import Tenant
from payments.models import Payment

def dashboard(request):
  context = {
    'contracts_count': Contract.objects.count(),
    'tenants_count': Tenant.objects.count(),
    'total_paid': Payment.objects.aggregate(Sum('amount'))['amount__sum'] or 0,
  }
  return render(request, 'core/dashboard.html', context)