from django.db import models
from django.utils.translation import gettext_lazy as _

class Unit(models.Model):
  name = models.CharField(
    max_length=100,
    verbose_name=_('اسم الوحدة')
  )
  floor = models.IntegerField(
    verbose_name=_('الطابق')
  )
  building_name = models.CharField(
    max_length=255,
    verbose_name=_('اسم المبنى')
  )
  is_occupied = models.BooleanField(
    default=False,
    verbose_name=_('مشغولة؟')
  )

  class Meta:
    verbose_name = _('وحدة')
    verbose_name_plural = _('الوحدات')

  def __str__(self):
    return f'{self.building_name} - طابق {self.floor} - {self.name}'