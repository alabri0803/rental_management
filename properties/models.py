from django.db import models

from users.models import Owner


class Property(models.Model):
  """نموذج العقار"""
  PROPERTY_TYPES = [
    ('apartment', 'شقة'),
    ('villa', 'فيلا'),
    ('office', 'مكتب'),
    ('shop', 'محل تجاري'),
    ('warehouse', 'مستودع')
  ]
  owner = models.ForeignKey(
    Owner,
    on_delete=models.CASCADE,
    verbose_name="المالك"
  )
  property_type = models.CharField(
    max_length=20,
    choices=PROPERTY_TYPES,
    verbose_name="نوع العقار"
  )
  title = models.CharField(
    max_length=200,
    verbose_name="عنوان العقار"
  )
  description = models.TextField(
    verbose_name="وصف العقار"
  )
  # تفاصيل الموقع
  area = models.CharField(
    max_length=100,
    verbose_name="المنطقة"
  )
  street = models.CharField(
    max_length=100,
    verbose_name="الشارع"
  )
  building_number = models.CharField(
    max_length=20,
    verbose_name="رقم المبنى"
  )
  floor_number = models.CharField(
    max_length=10,
    verbose_name="رقم الطابق"
  )
  apartment_number = models.CharField(
    max_length=10,
    verbose_name="رقم الشقة"
  )
  # تفاصيل العقار
  bedrooms = models.PositiveIntegerField(
    verbose_name="عدد الغرف النوم"
  )
  bathrooms = models.PositiveIntegerField(
    verbose_name="عدد دورات المياه"
  )
  area_sqm = models.DecimalField(
    max_digits=8,
    decimal_places=2,
    verbose_name="المساحة (متر مربع)"
  )
  # تفاصيل الإيجار
  monthly_rent = models.DecimalField(
    max_digits=10,
    decimal_places=3,
    verbose_name="الإيجار الشهري (ريال عماني)"
  )
  security_deposit = models.DecimalField(
    max_digits=10,
    decimal_places=3,
    verbose_name=" التأمين (ريال عماني)"
  )
  # المرافق
  has_parking = models.BooleanField(
    default=False,
    verbose_name="موقف سيارات"
  )
  has_elevator = models.BooleanField(
    default=False,
    verbose_name="مصعد"
  )
  has_balcony = models.BooleanField(
    default=False,
    verbose_name="شرفة"
  )
  has_garden = models.BooleanField(
    default=False,
    verbose_name="حديقة"
  )
  # حالة العقار
  is_available = models.BooleanField(
    default=True,
    verbose_name="متاح للإيجار"
  )
  created_at = models.DateTimeField(
    auto_now_add=True,
    verbose_name="تاريخ الإنشاء"
  )
  updated_at = models.DateTimeField(
    auto_now=True,
    verbose_name="تاريخ التحديث"
  )

  def __str__(self):
    return f"{self.title} - {self.area}"

  def calulate_registration_fees(self):
    """حساب رسوم تسجيل العقد"""
    annual_rent = self.monthly_rent * 12
    admin_fees = annual_rent * 0.03
    office_fees = 1
    additional_fees = 5
    total_fees = admin_fees + office_fees + additional_fees
    return {
      'admin_fees': admin_fees,
      'office_fees': office_fees,
      'additional_fees': additional_fees,
      'total_fees': total_fees
    }

  class Meta:
    verbose_name = "عقار"
    verbose_name_plural = "العقارات"

class PropertyImage(models.Model):
  """صور العقار"""
  property = models.ForeignKey(
    Property,
    on_delete=models.CASCADE,
    related_name='images',
    verbose_name="العقار"
  )
  image = models.ImageField(
    upload_to='property_images/',
    verbose_name="الصورة"
  )
  caption = models.CharField(
    max_length=200,
    blank=True,
    verbose_name="وصف الصورة"
  )
  is_main = models.BooleanField(
    default=False,
    verbose_name="الصورة الرئيسية"
  )

  def __str__(self):
    return f"صورة {self.property.title}"

  class Meta:
    verbose_name = "صورة عقار"
    verbose_name_plural = "صور العقارات"