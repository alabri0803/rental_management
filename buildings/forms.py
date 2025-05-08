from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Unit

class UnitForm(forms.ModelForm):
  class Meta:
    model = Unit
    fields = ['floor', 'unit_number', 'unit_type', 'area', 'is_available']
    labels = {
      'floor': _('الطابق'),
      'unit_number': _('رقم الوحدة'),
      'unit_type': _('نوع الوحدة'),
      'area': _('المساحة (م2)'),
      'is_available': _('متاحة للتأجير'),
    }
    widgets = {
      'floor': forms.Select(attrs={'class': 'form-control'}),
      'unit_number': forms.TextInput(attrs={'class': 'form-control'}),
      'unit_type': forms.Select(attrs={'class': 'form-control'}),
      'area': forms.NumberInput(attrs={'class': 'form-control'}),
      'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    }