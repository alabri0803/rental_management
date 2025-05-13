from django.db import models
from django.utils.translation import gettext_lazy as _

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

class PropertyPuropse(models.TextChoices):
  REINVEST = 'REINV', _('استثمار لإعادة التأجير')
  COMMERCIAL = 'COM', _('تجاري')
  RESIDENTIAL = 'RES', _('سكني')
  INDUSTRIAL = 'IND', _('صناعي')

class UsageType(models.TextChoices):
  FAMILY = 'FAM', _('سكن عائلي')
  LABOUR = 'LAB', _('سكن قوى عاملة')
  STUDENT = 'STU', _('سكن طلاب')
  FEMALE_STUDENT = 'FSTU', _('سكن طالبات')