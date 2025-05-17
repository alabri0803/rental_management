from django.shortcuts import render
from contracts.models import Contract
from tenants.models import Tenant
from payments.models import Payment
from buildings.models import Unit
from django.db.models import Sum

def dashboard(request):
  context = {
    'active_contracts': Contract.objects.count(),
    'tenants_count': Tenant.objects.count(),
    'total_payments': Payment.objects.aggregate(Sum('amount'))['amount__sum'] or 0,
    'available_units': Unit.objects.filter(is_occupied=False).count(),
  }
  return render(request, 'dashboard.html', context)