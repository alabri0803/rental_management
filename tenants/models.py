from django.db import models
from django.utils.translation import gettext_lazy as _

class Tenant(models.Model):
  full_name = models.CharField(
    max_length=255, 
    verbose_name=_("الاسم الكامل")
  )
  national_id = models.CharField(
    max_length=20, 
    verbose_name=_("الرقم المدني / الهوية")
  )
  phone = models.CharField(
    max_length=20, 
    verbose_name=_("رقم الهاتف")
  )
  email = models.EmailField(
    blank=True,  
    null=True,
    max_length=255, 
    verbose_name=_("البريد الالكتروني")
  )
  address = models.TextField(
    blank=True,
    null=True,
    verbose_name=_("العنوان")
  )

  created_at = models.DateTimeField(
    auto_now_add=True,
    verbose_name=_("تاريخ الإنشاء")
  )
  updated_at = models.DateTimeField(
    auto_now=True,
    verbose_name=_("آخر تعديل")
  )

  class Meta:
    verbose_name = _("مستأجر")
    verbose_name_plural = _("المستأجرون")

  def __str__(self):
    return self.full_name