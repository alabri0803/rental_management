from django.contrib import admin

from .models import Property, PropertyImage


class PropertyImageInline(admin.TabularInline):
  """إدارة صور العقار داخل صفحة العقار"""
  model = PropertyImage
  extra = 1

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
  """إدارة العقارات"""
  list_display = ('title', 'property_type', 'area', 'monthly_rent', 'owner', 'is_available', 'created_at')
  search_fields = ('title', 'area', 'street', 'owner__user__first_name', 'owner__user__last_name')
  readonly_fields = ('created_at', 'updated_at')
  inlines = [PropertyImageInline]
  fieldsets = (
    ('معلومات أساسية', {
      'fields': ('owner', 'property_type', 'title', 'description')
    }),
    ('الموقع', {
      'fields': ('area', 'street', 'building_number', 'floor_number', 'apartment_number')
    }),
    ('تفاصيل العقار', {
      'fields': ('bedrooms', 'bathrooms', 'area_sqm')
    }),
    ('الإيجار', {
      'fields': ('monthly_rent', 'security_deposit')
    }),
    ('المرافق', {
      'fields': ('has_parking', 'has_elevator', 'has_balcony', 'has_garden')
    }),
    ('الحالة', {
      'fields': ('is_available',)
    }),
    ('التواريخ', {
      'fields': ('created_at', 'updated_at')
    })
  )
  def get_queryset(self, request):
    return super().get_queryset(request).select_related('owner__user')

@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
  """إدارة صور العقارات"""
  list_display = ('property', 'caption', 'is_main', 'image')
  list_filter = ('is_main', 'property__property_type')
  search_fields = ('property__title', 'caption')