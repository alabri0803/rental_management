from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.mail import EmailMessage

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

    # استخدام render_to_string بدلاً من get_template.render
    html_string = render_to_string(
        'contracts/contract_pdf.html',
        {'contract': contract}
    )

    # إنشاء كائن HTML
    html = HTML(string=html_string, base_url=request.build_absolute_uri())

    # تهيئة الخطوط
    font_config = FontConfiguration()

    # إضافة CSS إضافي إذا لزم الأمر
    css = CSS(string='''
        @page {
            size: A4;
            margin: 1.5cm;
            @top-right {
                content: "العقد رقم: " counter(page) " من " counter(pages);
                font-size: 10pt;
            }
        }
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
        }
        .contract-header {
            text-align: center;
            margin-bottom: 20px;
        }
        .contract-title {
            font-size: 18pt;
            font-weight: bold;
            color: #2c3e50;
        }
    ''', font_config=font_config)

    # إنشاء ملف PDF
    pdf_file = html.write_pdf(stylesheets=[css], font_config=font_config)

    # إعداد الاستجابة
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="contract_{contract.contract_number}.pdf"'

    return response
