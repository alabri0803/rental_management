from django.contrib import admin
from .models import Governorate, Wilayat, Building, Floor, Unit
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter

class CustomAdminSite(admin.AdminSite):
  site_header = _("نظام إدارة العقارات - عُمان")
  site_title = _("إدارة العقارات")
  index_title = _("مرحبا بكم في الإدارة")

custom_admin_site = CustomAdminSite(name='custom_admin')

class GovernorateAdmin(ImportExportModelAdmin):
  list_display = ('name', 'code', 'is_active')
  list_editable = ('is_active',)
  search_fields = ('name', 'code')
  list_filter = ('is_active',)
  ordering = ('name',)

@admin.register(Wilayat, site=CustomAdminSite())
class WilayatAdmin(ImportExportModelAdmin):
  list_display = ('name', 'governorate', 'code', 'postal_code', 'is_active')
  list_editable = ('is_active', 'postal_code')
  search_fields = ('name', 'code', 'postal_code')
  list_filter = (('governorate', RelatedDropdownFilter), 'is_active')
  ordering = ('governorate__name', 'name')

class FloorInline(admin.TabularInline):
  model = Floor
  extra = 0
  fields = ('number', 'description', 'floor_plan')
  readonly_fields = ('created_at', 'updated_at')

@admin.register(Building, site=CustomAdminSite())
class BuildingAdmin(ImportExportModelAdmin):
  list_display = ('name', 'building_type', 'governorate', 'wilayat', 'owner_name', 'owner_phone')
  list_filter = ('building_type', ('governorate', RelatedDropdownFilter), 'wilayat')
  search_fields = ('name', 'address', 'owner_name', 'owner_phone')
  inlines = [FloorInline]
  fieldsets = (
    (_("المعلومات الأساسية"), {
      'fields': ('name', 'building_type', 'governorate', 'wilayat')
    }),
    (_("تفاصيل الموقع"), {
      'fields': ('address', 'location_link')
    }),
    (_("معلومات المالك"), {
      'fields': ('owner_name', 'owner_phone')
    }),
  )
  

class UnitInline(admin.TabularInline):
  model = Unit
  extra = 0
  fields = ('unit_number', 'unit_type', 'area', 'monthly_rent', 'is_available')
  readonly_fields = ('created_at', 'updated_at')

@admin.register(Floor, site=CustomAdminSite())
class FloorAdmin(ImportExportModelAdmin):
  list_display = ('building', 'number', 'units_count')
  list_filter = (('building', RelatedDropdownFilter),)
  inlines = [UnitInline]
  search_fields = ('building__name', 'number')

  def units_count(self, obj):
    return obj.units.count()
  units_count.short_description = _("عدد الوحدات")

@admin.register(Unit, site=CustomAdminSite())
class UnitAdmin(ImportExportModelAdmin):
  list_display = ('unit_number', 'unit_type', 'floor', 'area', 'is_available')
  list_filter = ('unit_type', 'is_available', ('floor__building', RelatedDropdownFilter),)
  search_fields = ('unit_number',)
  list_editable = ('is_available', 'monthly_rent')
  readonly_fields = ('created_at', 'updated_at')
  fieldsets = (
    (_("المعلومات الأساسية"), {
      'fields': ('floor', 'unit_number', 'unit_type')
    }),
    (_("تفاصيل الوحدة"), {
      'fields': ('area', 'monthly_rent', 'is_available')
    }),
    (_("مميزات إضافية"), {
      'fields': ('features',)
    }),
  )
custom_admin_site.register(Governorate, GovernorateAdmin)