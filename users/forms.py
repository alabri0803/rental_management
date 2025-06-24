from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, Owner, Tenant


class CustomUserCreationForm(UserCreationForm):
  """نموذج إنشاء مستخدم جديد"""
  email = forms.EmailField(
    required=True,
    label="البريد الإلكتروني"
  )
  firs_name = forms.CharField(
    max_length=30,
    required=True,
    label="الاسم الأول"
  )
  last_name = forms.CharField(
    max_length=30,
    required=True,
    label="اسم العائلة"
  )
  phone = forms.CharField(
    max_length=20,
    required=True,
    label="رقم الهاتف"
  )
  address = forms.CharField(
    widget=forms.Textarea(attrs={'rows': 3}),
    label="العنوان"
  )
  class Meta:
    model = CustomUser
    fields = ('username', 'email', 'first_name', 'last_name', 'phone', 'address', 'preferred_language')
    labels = {
      'username': 'اسم المستخدم',
      'preferred_language': 'اللغة المفضلة'
    }
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # إضافة classes CSS للتنسيق
    for field_name, field in self.fields.items():
      field.widget.attrs['class'] = 'form-control'
      if field_name in ['password1', 'password2']:
        field.label = 'كلمة المرور' if field_name == 'password1' else 'تأكيد كلمة المرور'

class OwnerForm(forms.ModelForm):
  """نموذج بيانات المالك"""
  class Meta:
    model = Owner
    fields = ('national_id', 'civil_id_copy')
    labels = {
      'national_id': 'الرقم المدني',
      'civil_id_copy': 'صورة الهوية المدنية'
    }
    widgets = {
      'national_id': forms.TextInput(attrs={'placeholder': 'أدخل الرقم المدني'}),
      'civil_id_copy': forms.FileInput(attrs={'accept': 'image/*'})
    }

class TenantForm(forms.ModelForm):
  """نموذج بيانات المستأجر"""
  class Meta:
    model = Tenant
    fields = ('national_id', 'civil_id_copy', 'employer', 'monthly_income')
    labels = {
      'national_id': 'الرقم المدني/السجل التجاري',
      'civil_id_copy': 'صورة الهوية المدنية',
      'employer': 'جهة العمل/صفته في السجل التجاري',
      'monthly_income': 'الدخل الشهري'
    }
    widgets = {
      'national_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل الرقم المدني أو السجل التجاري'}),
      'civil_id_copy': forms.FileInput(attrs={'class': 'form-control'}),
      'employer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل جهة العمل أو صفته في السجل التجاري'}),
      'monthly_income': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001', 'placeholder': '0.000'}),
    }

class UserProfileForm(forms.ModelForm):
  """نموذج تحديث ملف المستخدم"""
  class Meta:
    model = CustomUser
    fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'preferred_language')
    labels = {
      'first_name': 'الاسم الأول',
      'last_name': 'اسم العائلة',
      'email': 'البريد الإلكتروني',
      'phone': 'رقم الهاتف',
      'address': 'العنوان',
      'preferred_language': 'اللغة المفضلة'
    }
    widgets = {
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'phone': forms.TextInput(attrs={'class': 'form-control'}),
      'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
      'preferred_language': forms.Select(attrs={'class': 'form-control'})
    }