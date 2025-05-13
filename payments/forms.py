from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
  class Meta:
    model = Payment
    fields = '__all__'
    widgets = {
      'date': forms.DateInput(attrs={'type': 'date'}),
    }