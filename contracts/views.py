from django.shortcuts import render, redirect, get_object_or_404
from .models import Contract
from .forms import ContractForm
from django.http import HttpResponse


def contract_list(request):
  contracts = Contract.objects.all()
  return render(request, 'contracts/contract_list.html', {'contracts': contracts})

def contract_detail(request, pk):
  contract = get_object_or_404(Contract, pk=pk)
  return render(request, 'contracts/contract_detail.html', {'contract': contract})

def contract_create(request):
  form = ContractForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('contract_list')
  return render(request, 'contracts/contract_form.html', {'form': form})

def contract_update(request, pk):
  contract = get_object_or_404(Contract, pk=pk)
  form = ContractForm(request.POST or None, instance=contract)
  if form.is_valid():
    form.save()
    return redirect('contract_list')
  return render(request, 'contracts/contract_form.html', {'form': form})
