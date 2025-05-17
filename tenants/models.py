from django.db import models
from django.utils.translation import gettext_lazy as _

class TenantStatus(models.TextChoices):
  ACTIVE = 'AC', _('نشط')
  LEFT = 'LF', _('منسحب')
  LATE = 'LT', _('متأخر عن السداد')

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
  photo_id = models.ImageField(
    upload_to='tenants_ids/',
    blank=True,
    null=True,
    verbose_name=_("صورة الهوية")
  )
  status = models.CharField(
    max_length=2,
    choices=TenantStatus.choices,
    default=TenantStatus.ACTIVE,
    verbose_name=_("الحالة")
  )

  def __str__(self):
    return self.full_name
    
  class Meta:
    verbose_name = _("مستأجر")
    verbose_name_plural = _("المستأجرون")
