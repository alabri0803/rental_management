from django import forms
from .models import Unit

class UnitForm(forms.ModelForm):
  class Meta:
    model = Unit
    fields = '__all__'
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'floor': forms.NumberInput(attrs={'class': 'form-control'}),
      'building_name': forms.TextInput(attrs={'class': 'form-control'}),
      'type': forms.Select(attrs={'class': 'form-select'}),
      'is_occupied': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'is_furnished': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'area': forms.NumberInput(attrs={'class': 'form-control'}),
      'coordinates': forms.TextInput(attrs={'class': 'form-control'}),
      'field_name': forms.TextInput(attrs={'class': 'form-control'}),
    }