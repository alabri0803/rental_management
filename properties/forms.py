from django import forms

from .models import Property, PropertyImage


class PropertyForm(forms.ModelForm):
  """نموذج إنشاء/تعديل عقار"""
  class Meta:
    model = Property
    exclude = ['owner', 'created_at', 'updated_at']
    labels = {
      'property_type': 'نوع العقار',
      'title': 'عنوان العقار',
      'description': 'وصف العقار',
      'area': 'المنطقة',
      'street': 'الشارع',
      'building_number': 'رقم المبنى',
      'floor_number': 'رقم الطابق',
      'apartment_number': 'رقم الشقة',
      'bedrooms': 'عدد الغرف النوم',
      'bathrooms': 'عدد دورات المياه',
      'area_sqm': 'المساحة (متر مربع)',
      'monthly_rent': 'الإيجار الشهري (ريال عماني)',
      'security_deposit': 'التأمين (ريال عماني)',
      'has_parking': 'موقف سيارات',
      'has_elevator': 'مصعد',
      'has_balcony': 'شرفة',
      'has_garden': 'حديقة',
      'is_available': 'متاح للإيجار'
    }
    widgets = {
      'property_type': forms.Select(attrs={'class': 'form-control'}),
      'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل عنوان العقار'}),
      'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'وصف تفصيلي للعقار'}),
      'area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'المنطقة'}),
      'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الشارع'}),
      'building_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم المبنى'}),
      'floor_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم الطابق'}),
      'apartment_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم الشقة'}),
      'bedrooms': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
      'bathrooms': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
      'area_sqm': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
      'monthly_rent': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001', 'placeholder': '0.000'}),
      'security_deposit': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001', 'placeholder': '0.000'}),
      'has_parking': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'has_elevator': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'has_balcony': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'has_garden': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    }

class PropertyImageForm(forms.ModelForm):
  """نموذج صورة عقار"""
  class Meta:
    model = PropertyImage
    fields = ['image', 'caption', 'is_main']
    labels = {
      'image': 'الصورة',
      'caption': 'وصف الصورة',
      'is_main': 'الصورة الرئيسية'
    }
    widgets = {
      'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
      'caption': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'وصف الصورة'}),
      'is_main': forms.CheckboxInput(attrs={'class': 'form-check-input'})
    }

class PropertySearchForm(forms.Form):
  """نموذج البحث في العقارات"""
  PROPERTY_TYPES = [
    ('', 'جميع الأنواع'),
  ] + Property.PROPERTY_TYPE_CHOICES
  search_query = forms.CharField(
    max_length=200,
    required=False,
    label='البحث',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ابحث في العقارات...'})
  )
  property_type = forms.ChoiceField(
    choices=PROPERTY_TYPES,
    required=False,
    label='نوع العقار',
    widget=forms.Select(attrs={'class': 'form-control'})
  )
  area = forms.CharField(
    max_length=100,
    required=False,
    label='المنطقة',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'المنطقة'})
  )
  min_rent = forms.DecimalField(
    max_digits=10,
    decimal_places=3,
    required=False,
    label='الحد الأدني للإيجار',
    widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001', 'placeholder': '0.000'})
  )
  max_rent = forms.DecimalField(
    max_digits=10,
    decimal_places=3,
    required=False,
    label='الحد الأقصى للإيجار',
    widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001', 'placeholder': '0.000'})
  )
  min_bedrooms = forms.IntegerField(
    required=False,
    label='الحد الأدنى للغرف النوم',
    widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 0})
  )
  has_parking = forms.BooleanField(
    required=False,
    label='موقف سيارات',
    widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
  )
  has_elevator = forms.BooleanField(
    required=False,
    label='مصعد',
    widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
  )
  is_available = forms.BooleanField(
    required=False,
    initial=True,
    label='متاح للإيجار',
    widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
  )