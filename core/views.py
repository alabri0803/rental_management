from django.shortcuts import render
from contracts.models import Contract
from tenants.models import Tenant
from payments.models import Payment
from buildings.models import Unit
from django.db.models import Sum

def dashboard(request):
  context = {
    'contracts_count': Contract.objects.count(),
    'tenants_count': Tenant.objects.count(),
    'units_total': Unit.objects.count(),
    'units_occupied': Unit.objects.filter(is_occupied=True).count(),
    'total_paid': Payment.objects.aggregate(Sum('amount'))['amount__sum'] or 0,
  }
  return render(request, 'dashboard.html', context)