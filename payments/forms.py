from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
  class Meta:
    model = Payment
    fields = '__all__'
    widgets = {
      'contract': forms.Select(attrs={'class': 'form-select'}),
      'amount': forms.NumberInput(attrs={'class': 'form-control'}),
      'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
      'method': forms.Select(attrs={'class': 'form-select'}),
      'receipt': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }