from django.db import models
from django.utils.translation import gettext_lazy as _

class UnitType(models.TextChoices):
  APARTMENT = 'AP', _('شقة')
  VILLA = 'VI', _('فيلا')
  SHOP = 'SH', _('محل')
  BILLBOARD = 'BLB', _('لوحة اعلانية')
  OFFICE = 'OFF', _('مكتب')
  MALL = 'MAL', _('مول')

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
  type = models.CharField(
    max_length=4,
    choices=UnitType.choices,
    verbose_name=_('نوع الوحدة')
  )
  is_occupied = models.BooleanField(
    default=False,
    verbose_name=_('مشغولة؟')
  )
  is_furnished = models.BooleanField(
    default=False,
    verbose_name=_('مؤثثة؟')
  )
  area = models.DecimalField(
    max_digits=7,
    decimal_places=2,
    verbose_name=_('المساحة (م2)')
  )
  coordinates = models.CharField(
    max_length=100,
    blank=True,
    null=True,
    verbose_name=_('الإحداثيات')
  )

  def __str__(self):
    return f'{self.building_name} - {self.name}'

  class Meta:
    verbose_name = _("وحدة")
    verbose_name_plural = _("الوحدات")