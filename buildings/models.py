from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

class Governorate(models.Model):
  """المحافظات العُمانية"""
  name = models.CharField(
    max_length=50,
    verbose_name=_("المحافظة")
  )
  code = models.CharField(
    max_length=3,
    unique=True,
    verbose_name=_("الكود")
  )
  is_active = models.BooleanField(
    default=True,
    verbose_name=_("نشطة")
  )

  class Meta:
    verbose_name = _("محافظة")
    verbose_name_plural = _("محافظات")
    ordering = ['name']

  def __str__(self):
    return self.name

class Wilayat(models.Model):
  """الولايات العُمانية"""
  governorate = models.ForeignKey(
    Governorate,
    on_delete=models.PROTECT,
    verbose_name=_("المحافظة")
  )
  name = models.CharField(
    max_length=50,
    verbose_name=_("الولاية")
  )
  code = models.CharField(
    max_length=6,
    unique=True,
    verbose_name=_("الكود")
  )
  postal_code = models.CharField(
    max_length=10,
    blank=True,
    verbose_name=_("الرمز البريدي")
  )
  is_active = models.BooleanField(
    default=True,
    verbose_name=_("نشطة")
  )

  class Meta:
    verbose_name = _("ولاية")
    verbose_name_plural = _("ولايات")
    ordering = ['governorate__name', 'name']
    constraints = [
      models.UniqueConstraint(
        fields=['governorate', 'name'],
        name='unique_wilayat'
      )
    ]

  def __str__(self):
    return f"{self.name} - {self.governorate.name}"

class Building(models.Model):
  """نموذج المبني مع تفاصيل عُمانية"""
  BUILDING_TYPES = [
    ('RESIDENTIAL', _("سكني")),
    ('COMMERCIAL', _("تجاري")),
    ('MIXED', _("مختلط")),
    ('GOVERNMENTAL', _("حكومي")),
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
    on_delete=models.PROTECT,
    null=True,
    verbose_name=_("المحافظة")
  )
  wilayat = models.ForeignKey(
    Wilayat,
    on_delete=models.PROTECT,
    null=True,
    verbose_name=_("الولاية")
  )
  address = models.TextField(
    verbose_name=_("العنوان التفصيلي")
  )
  location_link = models.URLField(
    blank=True,
    verbose_name=_("رابط الموقع على خرائط Google")
  )
  owner_name = models.CharField(
    max_length=100,
    blank=True,
    verbose_name=_("اسم المالك")
  )
  owner_phone = models.CharField(
    max_length=15,
    blank=True,
    verbose_name=_("رقم هاتف المالك")
  )
  created_at = models.DateTimeField(
    auto_now_add=True,
    verbose_name=_("تاريخ الإنشاء")
  )
  updated_at = models.DateTimeField(
    auto_now=True,
    verbose_name=_("تاريخ التحديث")
  )

  class Meta:
    verbose_name = _("مبنى")
    verbose_name_plural = _("مباني")
    ordering = ['-created_at']
    indexes = [
      models.Index(fields=['name']),
      models.Index(fields=['building_type']),
      models.Index(fields=['governorate', 'wilayat']),
    ]

  def __str__(self):
    return f"{self.name} - {self.wilayat.name}"

class Floor(models.Model):
  """طوابق المبنى"""
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
  floor_plan = models.ImageField(
    upload_to='floor_plans/',
    blank=True,
    verbose_name=_("خريطة الطابق")
  )

  class Meta:
    verbose_name = _("طابق")
    verbose_name_plural = _("طوابق")
    ordering = ['building', 'number']
    unique_together = ('building', 'number')
    constraints = [
      models.CheckConstraint(
        check=models.Q(number__gte=0),
        name='floor_number_positive'
      )
    ]

  def __str__(self):
    return f"{self.building.name} - {_('طابق')} {self.number}"

class Unit(models.Model):
  """الوحدات السكنية/التجارية"""
  UNIT_TYPES = [
    ('APARTMENT', _("شقة")),
    ('OFFICE', _("مكتب")),
    ('SHOP', _("محل تجاري")),
    ('VILLA', _("فيلا")),
    ('HALL', _("قاعة"))
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
    validators=[MinValueValidator(0)],
    verbose_name=_("المساحة (م2)")
  )
  monthly_rent = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    default=0,
    verbose_name=_("الإيجار الشهري (ر.ع.)")
  )
  is_available = models.BooleanField(
    default=True,
    verbose_name=_("متاحة للتأجير")
  )
  features = models.JSONField(
    default=dict,
    verbose_name=_("المميزات")
  )

  class Meta:
    verbose_name = _("وحدة")
    verbose_name_plural = _("وحدات")
    ordering = ['floor__building', 'floor__number', 'unit_number']
    constraints = [
      models.UniqueConstraint(
        fields=['floor', 'unit_number'],
        name='unique_unit_per_floor'
      )
    ]

  def __str__(self):
    return f"{self.floor.building.name} - {self.unit_number}"

  def get_absolute_url(self):
    from django.urls import reverse
    return reverse('buildings:unit_detail', args=[str(self.id)])