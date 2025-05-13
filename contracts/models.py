from django.db import models
from django.utils.translation import gettext_lazy as _
from tenants.models import Tenant
from buildings.models import Unit

class LessorType(models.TextChoices):
  AGREEMENT = 'AG', _('اتفاقة/شراكة')
  CR = 'CR', _('سجل تجاري')
  CV = 'CV', _('شخص')
  EM = 'EM', _('سفارة')
  FC = 'FC', _('شركة أجنبية')
  GV = 'GV', _('جهة حكومة')
  HT = 'HT', _('ورثة')
  PR = 'PR', _('سجل مهني')

class LessorRelation(models.TextChoices):
  INVESTOR = 'INV', _('مستثمر')
  BENEFICIARY = 'BEN', _('منتفع')

class PuropseOfContract(models.TextChoices):
  REINVEST = 'REINV', _('استثمار لإعادة التأجير')
  COMMERCIAL = 'COM', _('تجاري')
  RESIDENTIAL = 'RES', _('سكني')
  INDUSTRIAL = 'IND', _('صناعي')

class ResidentialUsageType(models.TextChoices):
  LABOUR_FAMILY = 'LF', _('سكن قوى عاملة - عائلي')
  LABOUR_SINGLE = 'LS', _('سكن قوى عاملة - عزابي')
  FAMILY = 'FAM', _('سكن عائلي')
  SINGLE = 'SIN', _('سكن عزابي')
  STUDENTS = 'STU', _('سكن طلاب')
  FEMALE_STUDENT = 'FSTU', _('سكن طالبات')

class LandUsagePurpose(models.TextChoices):
  AGRICULTURE = 'AGR', _('زراعي')
  COMMERCIAL = 'COM', _('تجاري')
  GOVERNMENT = 'GOV', _('حكومي')
  INDUSTRIAL = 'IND', _('صناعي')
  RESIDENTIAL = 'RES', _('سكني')
  MIXED = 'MIX', _('سكني تجاري')

class Contract(models.Model):
  lessor_name = models.CharField(max_length=255, verbose_name=_('اسم المؤجر'))
  lessor_type = models.CharField(max_length=3, choices=LessorType.choices, verbose_name=_('نوع المؤجر'))
  lessor_relation = models.CharField(max_length=3, choices=LessorRelation.choices, verbose_name=_('علاقة المؤجر'))

  is_lessor_owner_of_building = models.BooleanField(verbose_name=_('هل المؤجر هو مالك المبنى؟'))

  tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, verbose_name=_('المستأجر'))
  unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name=_('الوحدة'))

  contract_number = models.CharField(max_length=50, unique=True, verbose_name=_('رقم العقد'))
  start_date = models.DateField(verbose_name=_('تاريخ البداية'))
  end_date = models.DateField(verbose_name=_('تاريخ النهاية'))

  purpose_of_contract = models.CharField(max_length=10, choices=PuropseOfContract.choices, verbose_name=_('الغرض من العقد'))
  residential_usage = models.CharField(max_length=4, choices=ResidentialUsageType.choices, verbose_name=_('نوع السكن'))
  land_usage_puropose = models.CharField(max_length=4, choices=LandUsagePurpose.choices, verbose_name=_('الغرض من استعمال الأرض'))

  rent_amount = models.DecimalField(max_digits=12, decimal_places=3, verbose_name=_('قيمة الإيجار'))
  notes = models.TextField(blank=True, null=True, verbose_name=_('ملاحظات'))

  created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('تاريخ الإنشاء'))
  updated_at = models.DateTimeField(auto_now=True, verbose_name=_('تاريخ التحديث'))

  class Meta:
    verbose_name = _('عقد')
    verbose_name_plural = _('العقود')
    ordering = ['-created_at']

  def __str__(self):
    return f'{self.contract_number} - {self.tenant}'