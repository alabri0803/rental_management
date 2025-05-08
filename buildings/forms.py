from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Unit, Building, Floor, Governorate, Wilayat
from django.core.validators import MinValueValidator
from django.forms import inlineformset_factory

class UnitForm(forms.ModelForm):
  class Meta:
    model = Unit
    fields = ['floor', 'unit_number', 'unit_type', 'area', 'monthly_rent', 'is_available', 'features']
    widgets = {
      'floor': forms.Select(attrs={'class': 'form-control select2', 'data-placeholder': _("اختر الطابق")}),
      'unit_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _("مثال: 101 أو A1")}),
      'unit_type': forms.Select(attrs={'class': 'form-control select2'}),
      'area': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
      'monthly_rent': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
      'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'features': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': _("مثال: { 'parking': true, 'balcony': false }")}),
    }
    labels = {
      'floor': _("الطابق"),
      'unit_number': _("رقم الوحدة"),
      'unit_type': _("نوع الوحدة"),
      'area': _("المساحة (م2)"),
      'monthly_rent': _("الإيجار الشهري (ر.ع.)"),
      'is_available': _("متاحة للتأجير"),
      'features': _("مميزات إضافية"),
    }

  def clean_unit_number(self):
    unit_number = self.cleaned_data.get('unit_number')
    floor = self.cleaned_data.get('floor')
    if Unit.objects.filter(floor=floor, unit_number=unit_number).exists(pk=self.instance.pk).exists():
      raise forms.ValidationError(_("رقم الوحدة موجود بالفعل في هذا الطابق."))
    return unit_number

  def clean_monthly_rent(self):
    rent = self.cleaned_data.get('monthly_rent')
    if rent < 0:
      raise forms.ValidationError(_("يجب أن يكون الإيجار قيمة موجبة"))
    return rent

class BuildingFilterForm(forms.Form):
  governorate = forms.ModelChoiceField(
    queryset=Governorate.objects.filter(is_active=True),
    required=False,
    label=_("المحافظة"),
    widget=forms.Select(attrs={'class': 'form-control select2'}))
  wilayat = forms.ModelChoiceField(
    queryset=Wilayat.objects.filter(is_active=True),
    required=False,
    label=_("الولاية"),
    widget=forms.Select(attrs={'class': 'form-control select2'})
  )
  building_type = forms.ChoiceField(
    choices=Building.BUILDING_TYPES,
    required=False,
    label=_("نوع المبنى"),
    widget=forms.Select(attrs={'class': 'form-control select2'})
  )
  search = forms.CharField(
    required=False,
    label=_("بحث"),
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _("اسم المبنى أو العنوان أو اسم المالك")})
  )

FloorFormSet = inlineformset_factory(Building, Floor, fields=['number', 'description', 'floor_plan'], extra=1, can_delete=True)