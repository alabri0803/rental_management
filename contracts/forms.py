from django import forms
from .models import Contract
from django.utils.translation import gettext_lazy as _

class ContractForm(forms.ModelForm):
  class Meta:
    model = Contract
    fields = '__all__'
    widgets = {
      'start_date': forms.DateInput(attrs={'type': 'date'}),
      'end_date': forms.DateInput(attrs={'type': 'date'}),
    }
    labels = {
      'lessor_name': _('اسم المؤجر'),
      'contract_number': _('رقم العقد'),
    }