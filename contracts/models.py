from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from tenants.models import Tenant
from buildings.models import Unit
from datetime import date

class Contract(models.Model):
  tenant = models.ForeignKey(
    Tenant,
    on_delete=models.CASCADE,
    verbose_name=_('المستأجر')
  )
  unit = models.ForeignKey(
    Unit,
    on_delete=models.CASCADE,
    verbose_name=_('الوحدة')
  )
  start_date = models.DateField(
    verbose_name=_('تاريخ البداية')
  )
  end_date = models.DateField(
    verbose_name=_('تاريخ النهاية')
  )
  rent_amount = models.DecimalField(
    max_digits=10,
    decimal_places=3,
    verbose_name=_('الإيجار الشهري (ر.ع)')
  )
  activity = models.CharField(
    max_length=255,
    verbose_name=_('النشاط التجاري'),
    blank=True,
    null=True,
  )
  created_at = models.DateTimeField(
    auto_now_add=True,
    verbose_name=_('تاريخ الإنشاء')
  )
  update_at = models.DateTimeField(
    auto_now=True,
    verbose_name=_('آخر تحديث')
  )


  class Meta:
    verbose_name = _("عقد إيجار")
    verbose_name_plural = _("عقود الإيجار")
    ordering = ['-start_date']
  def __str__(self):
    return f"{self.contract_number} - {self.tenant.full_name}"

  @property
  def contract_duration_months(self):
    if self.start_date and self.end_date:
      return (self.end_date.year - self.start_date.year) * 12 + (self.end_date.month - self.start_date.month)
    return 0

  @property
  def months_remaining(self):
    today = date.today()
    if self.end_date and self.end_date >= today:
      return (self.end_date.year - today.year) * 12 + (self.end_date.month - today.month)
    return 0

  @property
  def admin_fee(self):
    return 1.000

  @property
  def office_fee(self):
    return 5.0000

  @property
  def registration_fee(self):
    return round((self.rent_amount * 0.03) * 12, 3) 

  @property
  def total_fees(self):
    return round(self.admin_fee + self.office_fee + self.registration_fee, 3)

  @property
  def contract_number(self):
    return f"CN-{self.id:044d}"
