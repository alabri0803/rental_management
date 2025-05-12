from django import forms
from .models import Unit

class UnitForm(forms.ModelForm):
  class Meta:
    model = Unit
    fields = ['building', 'unit_type', 'floor', 'number', 'size_sqm', 'is_available']
    widgets = {
      'building': forms.Select(attrs={'class': 'form-control'}),
      'unit_type': forms.Select(attrs={'class': 'form-control'}),
      'floor': forms.NumberInput(attrs={'class': 'form-control'}),
      'number': forms.TextInput(attrs={'class': 'form-control'}),
      'size_sqm': forms.NumberInput(attrs={'class': 'form-control'}),
      'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    }