from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.mail import EmailMessage
from weasyprint import HTML
from io import BytesIO
from weasyprint.text.fonts import FontConfiguration

from .models import Contract
from .forms import ContractForm

def contract_list(request):
  contracts = Contract.objects.all()
  return render(request, 'contracts/contract_list.html', {'contracts': contracts})

def contract_detail(request, pk):
  contract = get_object_or_404(Contract, pk=pk)
  return render(request, 'contracts/contract_detail.html', {'contract': contract})

def contract_create(request):
  form = ContractForm(request.POST or None, request.FILES or None)
  if form.is_valid():
    form.save()
    return redirect(reverse_lazy('contracts:list'))
  return render(request, 'contracts/contract_form.html', {'form': form})

def contract_update(request, pk):
  contract = get_object_or_404(Contract, pk=pk)
  form = ContractForm(request.POST or None, request.FILES or None, instance=contract)
  if form.is_valid():
    form.save()
    return redirect(reverse_lazy('contracts:detail', kwargs={'pk': pk}))
  return render(request, 'contracts/contract_form.html', {'form': form})

def contract_pdf(request, pk):
  contract = get_object_or_404(Contract, pk=pk)
  html_string = render_to_string('contracts/contract_pdf.html', {'contract':contract})
  font_config = FontConfiguration()
  html = HTML(string=html_string)
  pdf_file = html.write_pdf(font_config=font_config)
  response = HttpResponse(pdf_file, content_type='application/pdf')
  response['Content-Disposition'] = f'attachment; filename="contract_{contract.contract_number}.pdf"'
  return response

def send_contract_email(request, pk):
  contract = get_object_or_404(Contract, pk=pk)
  template = get_template('contracts/contract_pdf.html')
  html = template.render({'contract': contract})
  pdf = BytesIO()
  pisa.CreatePDF(html, dest=pdf)

  email = EmailMessage(
    subject=f"عقد رقم {contract.contract_number}",
    body="مرفق مع هذا البريد الإلكتروني هو عقد الإيجار.",
    to=[contract.tenant.email]
  )
  email.attach(f"contract_{contract.contract_number}.pdf", pdf.getvalue(), 'application/pdf')
  email.send()
  return redirect(reverse_lazy('contracts:detail', kwargs={'pk': pk}))
