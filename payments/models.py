from django.db import models
from django.utils.translation import gettext_lazy as _
from contracts.models import Contract

class PaymentMethod(models.TextChoices):
  CASH = 'CA', _('نقدي')
  BANK = 'BN', _('تحويل بنكي')
  CARD = 'CR', _('بطاقة')
  CHECK = 'CH', _('شيك')
  
class Payment(models.Model):
  contract = models.ForeignKey(
    Contract, 
    on_delete=models.CASCADE, 
    verbose_name=_('العقد')
  )
  amount = models.DecimalField(
    max_digits=10,
    decimal_places=3,
    verbose_name=_('المبلغ (ر.ع)')
  )
  date = models.DateField(
    verbose_name=_('تاريخ الدفع')
  )
  method = models.CharField(
    max_length=2,
    choices=PaymentMethod.choices,
    verbose_name=_('طريقة الدفع')
  )
  receipt = models.FileField(
    upload_to='receipts/',
    blank=True,
    null=True,
    verbose_name=_('إيصال الدفع')
  )

  def __str__(self):
    return f"{self.contract.contract_number} - {self.amount:.3f} ر.ع"

  class Meta:
    verbose_name = _("دفعة")
    verbose_name_plural = _("الدفعات")