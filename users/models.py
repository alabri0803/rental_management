from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
  """نموذج المستخدم المخصص"""
  LANGUAGE_CHOICES = [
    ('ar', 'العربية'),
    ('en', 'English'),
  ]
  phone = models.CharField(
    max_length=20,
    verbose_name="رقم الهاتف"
  )
  addres = models.TextField(
    verbose_name="العنوان"
  )
  preferred_language = models.CharField(
    max_length=2,
    choices=LANGUAGE_CHOICES,
    default='ar',
    verbose_name="اللغة المفضلة"
  )
  created_at = models.DateTimeField(
    auto_now_add=True,
    verbose_name="تاريخ الإنشاء"
  )
  updated_at = models.DateTimeField(
    auto_now=True,
    verbose_name="تاريخ التحديث"
  )

  class Meta:
    verbose_name = "مستخدم"
    verbose_name_plural = "المستخدمون"

class Owner(models.Model):
  """نموذج المالك"""
  user = models.OneToOneField(
    CustomUser,
    on_delete=models.CASCADE,
    verbose_name="المستخدم"
  )
  national_id = models.CharField(
    max_length=20,
    unique=True,
    verbose_name="الرقم المدني"
  )
  civil_id_copy = models.FileField(
    upload_to='civil_ids/',
    blank=True,
    verbose_name="صورة الهوية المدنية"
  )

  def __str__(self):
    return f"{self.user.first_name} {self.user.last_name}"

  class Meta:
    verbose_name = "مالك"
    verbose_name_plural = "الملاك"

class Tenant(models.Model):
  """نموذج المستأجر"""
  user = models.OneToOneField(
    CustomUser,
    on_delete=models.CASCADE,
    verbose_name="المستخدم"
  )
  national_id = models.CharField(
    max_length=20,
    unique=True,
    verbose_name="الرقم المدني/السجيل التجاري"
  )
  civil_id_copy = models.FileField(
    upload_to='civil_ids/',
    blank=True,
    verbose_name="صورة الهوية المدنية"
  )
  employer = models.CharField(
    max_length=200,
    blank=True,
    verbose_name="جهة العمل/صفته في السجل التجاري"
  )
  monthly_income = models.DecimalField(
    max_digits=10,
    decimal_places=3,
    blank=True,
    null=True,
    verbose_name="الدخل الشهري"
  )

  def __str__(self):
    return f"{self.user.first_name} {self.user.last_name}"

  class Meta:
    verbose_name = "مستأجر"
    verbose_name_plural = "المستأجرون"