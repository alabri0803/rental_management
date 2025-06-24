from django import forms
from django.core.exceptions import ValidationError

from .models import Contract, ContractCancellation, Document, Payment, UtilityCommitment


class ContractForm(forms.ModelForm):
  """نموذج إنشاء/تعديل عقد إيجار"""
  class Meta:
    model = Contract
    exclude = ['admin_fees', 'total_fees', 'created_at', 'updated_at', 'signed_at']
    labels = {
      'property': 'العقار',
      'owner': 'المالك',
      'tenant': 'المستأجر',
      'contract_number': 'رقم العقد',
      'start_date': 'تاريخ بداية العقد',
      'end_date': 'تاريخ انتهاء العقد',
      'monthly_rent': 'الإيجار الشهري (ريال عماني)',
      'security_deposit': 'التأمين (ريال عماني)',
      'office_fees': 'رسوم المكتب (ريال عماني)',
      'additional_fees': 'رسوم إضافية (ريال عماني)',
      'status': 'حالة العقد',
      'terms_and_conditions': 'الشروط والأحكام',
      'notes': 'ملاحظات'
    }
    widgets = {
      'property': forms.Select(attrs={'class': 'form-control'}),
      'owner': forms.Select(attrs={'class': 'form-control'}),
      'tenant': forms.Select(attrs={'class': 'form-control'}),
      'contract_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم العقد'}),
      'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
      'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
      'monthly_rent': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001', 'placeholder': '0.000'}),
      'security_deposit': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001', 'placeholder': '0.000'}),
      'office_fees': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001', 'placeholder': '0.000'}),
      'additional_fees': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001', 'placeholder': '0.000'}),
      'status': forms.Select(attrs={'class': 'form-control'}),
      'terms_and_conditions': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
      'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    }
    def clean(self):
      cleaned_data = super().clean()
      start_date = cleaned_data.get('start_date')
      end_date = cleaned_data.get('end_date')
      if start_date and end_date:
        if end_date <= start_date:
          raise ValidationError('تاريخ انتهاء العقد يجب أن يكون بعد تاريخ البداية.')
      return cleaned_data

class PaymentForm(forms.ModelForm):
  """نموذج إضافة/تعديل المدفوعات"""
  class Meta:
    model = Payment
    exclude = ['created_at', 'updated_at']
    labels = {
      'payment_type': 'نوع الدفع',
      'amount': 'المبلغ (ريال عماني)',
      'due_date': 'تاريخ الاستحقاق',
      'paid_date': 'تاريخ الدفع',
      'status': 'حالة الدفعة',
      'notes': 'ملاحظات'
    }
    widgets = {
      'payment_type': forms.Select(attrs={'class': 'form-control'}),
      'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001', 'placeholder': '0.000'}),
      'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
      'paid_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
      'status': forms.Select(attrs={'class': 'form-control'}),
      'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    }

class DocumentForm(forms.ModelForm):
  """نموذج رفع المستندات"""
  class Meta:
    model = Document
    exclude = ['created_at', 'updated_at']
    labels = {
      'contract': 'العقد',
      'document_type': 'نوع المستند',
      'title': 'عنوان المستند',
      'file': 'الملف',
      'description': 'الوصف'
    }
    widgets = {
      'contract': forms.Select(attrs={'class': 'form-control'}),
      'document_type': forms.Select(attrs={'class': 'form-control'}),
      'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان المستند'}),
      'file': forms.FileInput(attrs={'class': 'form-control'}),
      'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    }

class ContractCancellationForm(forms.ModelForm):
  """نموذج إلغاء العقد"""
  class Meta:
    model = ContractCancellation
    exclude = ['created_at']
    labels = {
      'contract': 'العقد',
      'cancellation_date': 'تاريخ الإلغاء',
      'reason': 'سبب الإلغاء',
      'owner_signature': 'توقيع المالك',
      'tenant_signature': 'توقيع المستأجر',
      'legal_responsibility_accepted': 'قبول المسؤولية القانونية'
    }
    widgets = {
      'contract': forms.Select(attrs={'class': 'form-control'}),
      'cancellation_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
      'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder':'اذكر سبب الغاء العقد'}),
      'owner_signature': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'tenant_signature': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'legal_responsibility_accepted': forms.CheckboxInput(attrs={'class': 'form-check-input'})
    }

class UtilityCommitmentForm(forms.ModelForm):
  """نموذج تعهد سداد المرافق"""
  class Meta:
    model = UtilityCommitment
    exclude = ['created_at']
    labels = {
      'contract': 'العقد',
      'electricity_commitment': 'تعهد سداد الكهرباء',
      'water_commitment': 'تعهد سداد الماء',
      'other_utilities': 'مرافق أخرى',
      'tenant_signature': 'توقيع المستأجر',
      'signature_date': 'تاريخ التوقيع'
    }
    widgets = {
      'contract': forms.Select(attrs={'class': 'form-control'}),
      'electricity_commitment': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'water_commitment': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'other_utilities': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'أدخل المرافق الأخرى'}),
      'tenant_signature': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'signature_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    }

class ContractSearchForm(forms.Form):
  """نموذج البحث في العقود"""
  STATUS_CHOICES = [
    ('', 'جميع الحالات')
  ] + Contract.STATUS_CHOICES
  search_query = forms.CharField(
    max_length=200,
    required=False,
    label='البحث',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ابحث برقم العقد أو اسم المالك أو المستأجر...'})
  )
  status = forms.ChoiceField(
    choices=STATUS_CHOICES,
    required=False,
    label='حالة العقد',
    widget=forms.Select(attrs={'class': 'form-control'})
  )
  start_date = forms.DateField(
    required=False,
    label='تاريخ البداية من',
    widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
  )
  end_date = forms.DateField(
    required=False,
    label='تاريخ البداية إلى',
    widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
  )
  property_area = forms.CharField(
    max_length=100,
    required=False,
    label='منطقة العقار',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'المنطقة'})
  )
  