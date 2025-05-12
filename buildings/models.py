from django.db import models
from django.utils.translation import gettext_lazy as _

class BuildingType(models.TextChoices):
  VILLA = 'villa', _('فيلا')
  HOUSE = 'house', _('بيت')
  APARTMENT_BUILDING = 'apartment_building', _('عمارة')
  COMMERCIAL = 'commercial', _('تجاري')
  RESIDENTIAL = 'residential', _('سكني')
  MIXED = 'mixed', _('تجاري وسكني')

class UnitType(models.TextChoices):
  SHOP = 'shop', _('محل تجاري')
  OFFICE = 'office', _('مكتب')
  APARTMENT = 'apartment', _('شقة')
  RESTAURANT = 'restaurant', _('مطعم')

class Building(models.Model):
  name = models.CharField(max_length=255)
  building_type = models.CharField(max_length=50, choices=BuildingType.choices)
  address = models.TextField()
  description = models.TextField(blank=True, null=True)

  def __str__(self):
    return self.name

class Unit(models.Model):
  building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='units')
  unit_type = models.CharField(max_length=50, choices=UnitType.choices)
  floor = models.IntegerField()
  number = models.CharField(max_length=50)
  size_sqm = models.DecimalField(max_digits=6, decimal_places=2)
  is_available = models.BooleanField(default=True)

  def __str__(self):
    return f"{self.building.name} - {self.unit_type} #{self.number}"