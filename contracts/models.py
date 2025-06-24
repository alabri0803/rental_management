from django.db import models
from django.utils import timezone

from properties.models import Property
from users.models import Owner, Tenant


class Contract(models.Model):
  """نموذج العقد الإيجار"""
  STATUS_CHOICES = [
    ('active', 'نشط'),
    ('expiring_soon', 'قريب من الانتهاء'),
    ('expired', 'منتهي'),
    ('cancelled', 'ملغي'),
    ('renewed', 'مجدد')
  ]
  # أطراف العقد
  property = models.ForeignKey(
    Property,
    on_delete=models.CASCADE,
    verbose_name="العقار"
  )
  owner = models.ForeignKey(
    Owner,
    on_delete=models.CASCADE,
    verbose_name="المالك"
  )
  tenant = models.ForeignKey(
    Tenant,
    on_delete=models.CASCADE,
    verbose_name="المستأجر"
  )
  # تفاصيل العقد
  contract_number = models.CharField(
    max_length=50,
    unique=True,
    verbose_name="رقم العقد"
  )
  start_date = models.DateField(
    default=timezone.now,
    verbose_name="تاريخ بداية العقد"
  )
  end_date = models.DateField(
    verbose_name="تاريخ انتهاء العقد"
  )
  monthly_rent = models.DecimalField(
    max_digits=10,
    decimal_places=3,
    verbose_name="الإيجار الشهري (ريال عماني)"
  )
  security_deposit = models.DecimalField(
    max_digits=10,
    decimal_places=3,
    verbose_name="التأمين (ريال عماني)"
  )
  # الرسوم
  admin_fees = models.DecimalField(
    max_digits=10,
    decimal_places=3,
    verbose_name="الرسوم الإدارية (ريال عماني)"
  )
  office_fees = models.DecimalField(
    max_digits=10,
    decimal_places=3,
    verbose_name="رسوم المكتب (ريال عماني)"
  )
  additional_fees = models.DecimalField(
    max_digits=10,
    decimal_places=3,
    verbose_name="رسوم إضافية (ريال عماني)"
  )
  total_fees = models.DecimalField(
    max_digits=10,
    decimal_places=3,
    verbose_name="إجمالي الرسوم (ريال عماني)"
  )
  # حالة العقد
  status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default='active',
    verbose_name="حالة العقد"
  )
  # شروط إضافية
  terms_and_conditions = models.TextField(
    verbose_name="الشروط والأحكام"
  )
  notes = models.TextField(
    blank=True,
    verbose_name="ملاحظات"
  )
  # تواريخ مهمة
  created_at = models.DateTimeField(
    auto_now_add=True,
    verbose_name="تاريخ الإنشاء"
  )
  updated_at = models.DateTimeField(
    auto_now=True,
    verbose_name="تاريخ التحديث"
  )
  signed_at = models.DateTimeField(
    blank=True,
    null=True,
    verbose_name="تاريخ التوقيع"
  )

  def save(self, *args, **kwargs):
    # حساب الرسوم تلقائيا
    if not self.admin_fees:
      annual_rent = self.monthly_rent * 12
      self.admin_fees = annual_rent * 0.03
      self.total_fees = self.admin_fees + self.office_fees + self.additional_fees
    # تحديث حالة العقد
    self.update_status()
    super().save(*args, **kwargs)

  def update_status(self):
    """تحديث حالة العقد بناءً على التاريخ """
    today = timezone.now().date()
    days_until_expiry = (self.end_date - today).days
    if self.status != 'cancelled':
      return # لا تحديث الحالة إذا كان العقد ملغي
    if today > self.end_date:
      self.status = 'expired'
    elif days_until_expiry <= 30:
      self.status = 'expiring_soon'
    else:
      self.status = 'active'

  def get_status_color(self):
    """إرجاع لون حالة العقد"""
    colors = {
      'active': '#28a745',
      'expiring_soon': '#ffc107',
      'expired': '#dc3545',
      'cancelled': '#6c757d',
      'renewed': '#17a2b8'
    }
    return colors.get(self.status, '#6c757d')

  def can_be_renewed(self):
    """التحقق من إمكانية تجديد العقد"""
    return self.status in ['active', 'expiring_soon', 'expired']

  def __str__(self):
    return f"عقد رقم {self.contract_number} - {self.property.title}"

  class Meta:
    verbose_name = "عقد إيجار"
    verbose_name_plural = "عقود الإيجار"
    ordering = ['-created_at']

class Payment(models.Model):
  """نموذج المدفوعات"""
  PAYMENT_TYPES = [
    ('rent', 'إيجار'),
    ('deposit', 'تأمين'),
    ('fees', 'رسوم'),
    ('utilities', 'مرافق')
  ]
  PAYMENT_STATUS = [
    ('pending', 'معلق'),
    ('paid', 'مدفوع'),
    ('overdue', 'متأخر'),
    ('cancelled', 'ملغي')
  ]
  contract = models.ForeignKey(
    Contract,
    on_delete=models.CASCADE,
    verbose_name="العقد"
  )
  payment_type = models.CharField(
    max_length=20,
    choices=PAYMENT_TYPES,
    verbose_name="نوع الدفع"
  )
  amount = models.DecimalField(
    max_digits=10,
    decimal_places=3,
    verbose_name="المبلغ (ريال عماني)"
  )
  due_date = models.DateField(
    verbose_name="تاريخ الاستحقاق"
  )
  paid_date = models.DateField(
    blank=True,
    null=True,
    verbose_name="تاريخ الدفع"
  )
  status = models.CharField(
    max_length=20,
    choices=PAYMENT_STATUS,
    default='pending',
    verbose_name="حالة الدفعة"
  )
  notes = models.TextField(
    blank=True,
    verbose_name="ملاحظات"
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
    return f"دفعة {self.get_payment_type_display()} - {self.amount} ريال"

  class Meta:
    verbose_name = "دفعة"
    verbose_name_plural = "المدفوعات"
    ordering = ['due_date']

class Document(models.Model):
  """نموذج المستندات"""
  DOCUMENT_TYPES = [
    ('contract', 'عقد إيجار'),
    ('cancellation', 'إلغاء عقد'),
    ('renewal', 'تجديد عقد'),
    ('commitment', 'تعهد سداد'),
    ('civil_id', 'هوية مدنية'),
    ('other', 'أخرى')
  ]
  contract = models.ForeignKey(
    Contract,
    on_delete=models.CASCADE,
    verbose_name="العقد"
  )
  document_type = models.CharField(
    max_length=20,
    choices=DOCUMENT_TYPES,
    verbose_name="نوع المستند"
  )
  title = models.CharField(
    max_length=200,
    verbose_name="عنوان المستند"
  )
  file = models.FileField(
    upload_to='documents/',
    verbose_name="الملف"
  )
  description = models.TextField(
    blank=True,
    verbose_name="الوصف"
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
    return f"{self.title} - {self.get_document_type_display()}"

  class Meta:
    verbose_name = "مستند"
    verbose_name_plural = "المستندات"
    ordering = ['-created_at']

class ContractCancellation(models.Model):
  """نموذج إلغاء العقد"""
  contract = models.OneToOneField(
    Contract,
    on_delete=models.CASCADE,
    verbose_name="العقد"
  )
  cancellation_date = models.DateField(
    verbose_name="تاريخ الإلغاء"
  )
  reason = models.TextField(
    verbose_name="سبب الإلغاء"
  )
  owner_signature = models.BooleanField(
    default=False,
    verbose_name="توقيع المالك"
  )
  tenant_signature = models.BooleanField(
    default=False,
    verbose_name="توقيع المستأجر"
  )
  # المسؤولية القانونية
  legal_responsibility_accepted = models.BooleanField(
    default=False,
    verbose_name="قبول المسؤولية القانونية"
  )
  created_at = models.DateTimeField(
    auto_now_add=True,
    verbose_name="تاريخ الإنشاء"
  )

  def __str__(self):
    return f"إلغاء عقد رقم {self.contract.contract_number}"

  class Meta:
    verbose_name = "إلغاء عقد"
    verbose_name_plural = "إلغاءات العقود"

class UtilityCommitment(models.Model):
  """نموذج تعهد سداد المرافق"""
  contract = models.ForeignKey(
    Contract,
    on_delete=models.CASCADE,
    verbose_name="العقد"
  )
  electricity_commitment = models.BooleanField(
    default=True,
    verbose_name="تعهد سداد الكهرباء"
  )
  water_commitment = models.BooleanField(
    default=True,
    verbose_name="تعهد سداد الماء"
  )
  other_utilities = models.TextField(
    blank=True,
    verbose_name="مرافق أخرى"
  )
  tenant_signature = models.BooleanField(
    default=False,
    verbose_name="توقيع المستأجر"
  )
  signature_date = models.DateField(
    blank=True,
    null=True,
    verbose_name="تاريخ التوقيع"
  )
  created_at = models.DateTimeField(
    auto_now_add=True,
    verbose_name="تاريخ الإنشاء"
  )

  def __str__(self):
    return f"تعهد سداد مرافق - عقد رقم {self.contract.contract_number}"

  class Meta:
    verbose_name = "تعهد سداد مرافق"
    verbose_name_plural = "تعهدات سداد المرافق"