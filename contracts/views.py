from django.shortcuts import render, redirect, get_object_or_404
from .models import Contract
from .forms import ContractForm
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.mail import EmailMessage

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

def contract_pdf(request, pk):
  contract = get_object_or_404(Contract, pk=pk)
  template = get_template('contracts/contract_pdf.html')
  html = template.render({'contract': contract})
  response = HttpResponse(content_type='application/pdf')
  response['Content-Disposition'] = f'attachment; filename="contract_{contract.id}.pdf"'
  pisa.CreatePDF(html, dest=response)
  return response

def send_contract_email(request, pk):
  contract = get_object_or_404(Contract, pk=pk)
  template = get_template('contracts/contract_email.html')
  html = template.render({'contract': contract})
  from io import BytesIO
  pdf = BytesIO()
  pisa.CreatePDF(html, dest=pdf)
  email = EmailMessage(
    subject=f"عقد إيجار رقم {contract.id}",
    body="مرفق نسخة PDF من العقد.",
    to=[contract.tenant.email],
  )
  email.attach(f"contract_{contract.contract_number}.pdf", pdf.getvalue(), 'application/pdf')
  email.send()
  return redirect('contract_list', pk=pk)