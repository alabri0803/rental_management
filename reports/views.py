from django.shortcuts import render
from contracts.models import Contract
from payments.models import Payment
from buildings.models import Unit
from django.db.models import Sum

def summary_report(request):
  context = {
    'contracts_total': Contract.objects.count(),
    'rent_total': Contract.objects.aggregate(Sum('rent_amount'))['rent_amount__sum'] or 0,
    'payments_total': Payment.objects.aggregate(Sum('amount'))['amount__sum'] or 0,
  }
  return render(request, 'reports/summary_report.html', context)

def occupancy_report(request):
  total = Unit.objects.count()
  occupied = Unit.objects.filter(is_occupied=True).count()
  vacant = total - occupied
  return render(request, 'reports/occupancy_report.html', {'total': total, 'occupied': occupied, 'vacant': vacant})

def revenue_report(request):
  payments = Payment.objects.all().order_by('date').annotate(total=Sum('amount')).order_by('date')
  return render(request, 'reports/revenue_report.html', {'payments': payments})