from django.db import models
from django.utils.translation import gettext_lazy as _

class Governorate(models.Model):
  name = models.CharField(
    max_length=50,
    verbose_name=_("المحافظة")
  )
  code = models.CharField(
    max_length=2,
    verbose_name=_("الكود")
  )

  class Meta:
    verbose_name = _("محافظة")
    verbose_name_plural = _("محافظات")

  def __str__(self):
    return self.name

class Wilayat(models.Model):
  governorate = models.ForeignKey(
    Governorate,
    on_delete=models.CASCADE,
    verbose_name=_("المحافظة")
  )
  name = models.CharField(
    max_length=50,
    verbose_name=_("الولاية")
  )
  code = models.CharField(
    max_length=2,
    verbose_name=_("الكود")
  )

  class Meta:
    verbose_name = _("ولاية")
    verbose_name_plural = _("ولايات")

  def __str__(self):
    return f"{self.name} - {self.governorate.name}"

class Building(models.Model):
  BUILDING_TYPES = [
    ('RESIDENTIAL', _("سكني")),
    ('COMMERCIAL', _("تجاري")),
    ('MIXED', _("مختلط")),
  ]
  name = models.CharField(
    max_length=100,
    verbose_name=_("اسم المبنى")
  )
  building_type = models.CharField(
    max_length=20,
    choices=BUILDING_TYPES,
    verbose_name=_("نوع المبنى")
  )
  governorate = models.ForeignKey(
    Governorate,
    on_delete=models.SET_NULL,
    null=True,
    verbose_name=_("المحافظة")
  )
  wilayat = models.ForeignKey(
    Wilayat,
    on_delete=models.SET_NULL,
    null=True,
    verbose_name=_("الولاية")
  )
  address = models.TextField(
    verbose_name=_("العنوان التفصيلي")
  )
  created_at = models.DateTimeField(
    auto_now_add=True,
    verbose_name=_("تاريخ الإنشاء")
  )

  class Meta:
    verbose_name = _("مبنى")
    verbose_name_plural = _("مباني")
    ordering = ['-created_at']

  def __str__(self):
    return self.name

class Floor(models.Model):
  building = models.ForeignKey(
    Building,
    on_delete=models.CASCADE,
    related_name='floors',
    verbose_name=_("المبنى")
  )
  number = models.PositiveIntegerField(
    verbose_name=_("رقم الطابق")
  )
  description = models.TextField(
    verbose_name=_("وصف الطابق")
  )

  class Meta:
    verbose_name = _("طابق")
    verbose_name_plural = _("طوابق")
    ordering = ['building', 'number']
    unique_together = ('building', 'number')

  def __str__(self):
    return f"{self.building.name} - {_('طابق')} {self.number}"

class Unit(models.Model):
  UNIT_TYPES = [
    ('APARTMENT', _("شقة")),
    ('OFFICE', _("مكتب")),
    ('SHOP', _("محل")),
    ('VILLA', _("فيلا")),
  ]
  floor = models.ForeignKey(
    Floor,
    on_delete=models.CASCADE,
    related_name='units',
    verbose_name=_("الطابق")
  )
  unit_number = models.CharField(
    max_length=20,
    verbose_name=_("رقم الوحدة")
  )
  unit_type = models.CharField(
    max_length=20,
    choices=UNIT_TYPES,
    verbose_name=_("نوع الوحدة")
  )
  area = models.DecimalField(
    max_digits=8,
    decimal_places=2,
    verbose_name=_("المساحة (م2)")
  )
  is_available = models.BooleanField(
    default=True,
    verbose_name=_("متاحة للتأجير")
  )

  class Meta:
    verbose_name = _("وحدة")
    verbose_name_plural = _("وحدات")
    ordering = ['floor__building', 'floor__number', 'unit_number']

  def __str__(self):
    return f"{self.floor.building.name} - {self.unit_number}"