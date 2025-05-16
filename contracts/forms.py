from django import forms
from .models import Contract
from django.utils.translation import gettext_lazy as _

class ContractForm(forms.ModelForm):
  class Meta:
    model = Contract
    fields = '__all__'
    widgets = {
      'contract_number': forms.TextInput(attrs={'class': 'form-control'}),
      'tenant': forms.Select(attrs={'class': 'form-select'}),
      'unit': forms.Select(attrs={'class': 'form-select'}),
      'start_date': forms.DateInput(attrs={'type': 'date'}),
      'end_date': forms.DateInput(attrs={'type': 'date'}),
      'rent_amount': forms.NumberInput(attrs={'class': 'form-control'}),
      'contract_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
      'status': forms.Select(attrs={'class': 'form-select'}),
      'contract_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }