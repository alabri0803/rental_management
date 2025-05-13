from django.db.models import Sum, Count
from django.shortcuts import render
from contracts.models import Contract
from payments.models import Payment

def summary_report(request):
  total_contracts = Contract.objects.count()
  total_rent = Contract.objects.aggregate(Sum('rent_amount'))['rent_amount__sum']
  total_paid = Payment.objects.aggregate(Sum('amount'))['amount__sum']
  return render(request, 'reports/summary_report.html', {
    'total_contracts': total_contracts,
    'total_rent': total_rent or 0,
    'total_paid': total_paid or 0,
  })

def occupancy_report(request):
  from buildings.models import Unit
  total_units = Unit.objects.count()
  occupied_units = Contract.objects.filter(is_occupied=True).count()
  return render(request, 'reports/occupancy_report.html', {
    'total_units': total_units,
    'occupied_units': occupied_units,
    'vacant_units': total_units - occupied_units
  })

def revenue_report(request):
  payments = Payment.objects.all().order_by('date').annotate(total=Sum('amount')).order_by('date')
  return render(request, 'reports/revenue_report.html', {'payments': payments})