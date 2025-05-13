from django.shortcuts import render, redirect, get_object_or_404
from .models import Contract
from .forms import ContractForm
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def contract_pdf(request, pk):
  contract = get_object_or_404(Contract, pk=pk)
  template = get_template('contracts/contract_pdf.html')
  context = {'contract': contract}
  html = template.render(context)
  response = HttpResponse(content_type='application/pdf')
  response['Content-Disposition'] = f'attachment; filename="contract_{contract.id}.pdf"'
  pisa.CreatePDF(html, dest=response)
  return response
      
def contract_list(request):
  contracts = Contract.objects.all()
  return render(request, 'contracts/contract_list.html', {'contracts': contracts})

def contract_detail(request, pk):
  contract = get_object_or_404(Contract, pk=pk)
  return render(request, 'contracts/contract_detail.html', {'contract': contract})

def contract_create(request):
  if request.method == 'POST':
    form = ContractForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('contract_list')
  else:
    form = ContractForm()
  return render(request, 'contracts/contract_form.html', {'form': form})

def contract_update(request, pk):
  contract = get_object_or_404(Contract, pk=pk)
  if request.method == 'POST':
    form = ContractForm(request.POST, instance=contract)
    if form.is_valid():
      form.save()
      return redirect('contract_list')
  else:
    form = ContractForm(instance=contract)
  return render(request, 'contracts/contract_form.html', {'form': form})