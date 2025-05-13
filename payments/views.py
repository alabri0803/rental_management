from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment
from .forms import PaymentForm

def payment_list(request):
  payments = Payment.objects.all()
  return render(request, 'payments/payment_list.html', {'payments': payments})

def payment_detail(request, pk):
  payment = get_object_or_404(Payment, pk=pk)
  return render(request, 'payments/payment_detail.html', {'payment': payment})

def payment_create(request):
  form = PaymentForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('payment_list')
  return render(request, 'payments/payment_form.html', {'form': form})

def payment_update(request, pk):
  payment = get_object_or_404(Payment, pk=pk)
  form = PaymentForm(request.POST or None, instance=payment)
  if form.is_valid():
    form.save()
    return redirect('payment_list', pk=payment.pk)
  return render(request, 'payments/payment_form.html', {'form': form})