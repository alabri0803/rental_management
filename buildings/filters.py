import django_filters
from django.utils.translation import gettext_lazy as _
from .models import Building, Governorate, Wilayat

class BuildingFilter(django_filters.FilterSet):
  name = django_filters.CharFilter(
    lookup_expr='icontains', 
    label=_("اسم المبنى")
  )
  governorate = django_filters.ModelChoiceFilter(
    field_name='governorate',
    label=_("المحافظة"),
    queryset=lambda 
    request: Governorate.objects.filter(is_active=True),
  )
  wilayat = django_filters.ModelChoiceFilter(
    field_name='wilayat',
    label=_("الولاية"),
    queryset=lambda
    request: Wilayat.objects.filter(is_active=True),
  )
  building_type = django_filters.ChoiceFilter(
    choices=Building.BUILDING_TYPES,
    label=_("نوع المبنى")
  )

  class Meta:
    model = Building
    fields = ['name', 'governorate', 'wilayat', 'building_type']