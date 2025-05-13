from django.db import models
from django.utils.translation import gettext_lazy as _
from contracts.models import Contract

class Payment(models.Model):
  contract = models.ForeignKey(
    Contract, 
    on_delete=models.CASCADE, 
    verbose_name=_('العقد')
  )
  amount = models.DecimalField(
    max_digits=12,
    decimal_places=3,
    verbose_name=_('المبلغ')
  )
  date = models.DateField(
    verbose_name=_('التاريخ الدفع')
  )
  notes = models.TextField(
    blank=True,
    null=True,
    verbose_name=_('ملاحظات')
  )

  class Meta:
    verbose_name = _('دفعة')
    verbose_name_plural = _('الدفعات')
    ordering = ['-date']

  def __str__(self):
    return f"{self.contract.contract_number} - {self.amount}"