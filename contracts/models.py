from django.db import models
from django.utils.translation import gettext_lazy as _
from tenants.models import Tenant
from buildings.models import Unit

class ContractStatus(models.TextChoices):
  ACTIVE = 'AC', _('ساري')
  ENDED = 'EN', _('منتهي')
  CANCELED = 'CA', _('ملغي')

class Contract(models.Model):
  contract_number = models.CharField(
    max_length=50,
    unique=True,
    verbose_name=_('رقم العقد')
  )
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
    verbose_name=_('الإيجار الشهري')
  )
  contract_file = models.FileField(
    upload_to='contracts/',
    blank=True,
    null=True,
    verbose_name=_('ملف العقد')
  )
  status = models.CharField(
    max_length=2,
    choices=ContractStatus.choices,
    default=ContractStatus.ACTIVE,
    verbose_name=_('الحالة')
  )

  def __str__(self):
    return f"{self.contract_number}"

  class Meta:
    verbose_name = _("عقد")
    verbose_name_plural = _("العقود")