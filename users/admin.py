from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Owner, Tenant


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
  """إدارة المستخدمين المخصصة"""
  list_display = ('username', 'email', 'first_name', 'last_name', 'phone', 'preferred_language', 'is_staff')
  list_filter = ('preferred_language', 'is_staff', 'is_active', 'date_joined')
  search_fields = ('username', 'email', 'first_name', 'last_name', 'phone')
  fieldsets = UserAdmin.fieldsets + (
    ('معلومات إضافية', {'fields': ('phone', 'addres', 'preferred_language')}),
  )

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
  """إدارة الملاك"""
  list_display = ('user', 'national_id', 'get_phone', 'get_email')
  search_fields = ('user__first_name', 'user__last_name', 'national_id', 'user__email')
  list_filter = ('user__date_joined',)

  def get_phone(self, obj):
    return obj.user.phone
  get_phone.short_description = 'رقم الهاتف'

  def get_email(self, obj):
    return obj.user.email
  get_email.short_description = 'البريد الإلكتروني'

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
  """إدارة المستأجرين"""
  list_display = ('user', 'national_id', 'employer', 'monthly_income', 'get_phone')
  search_fields = ('user__first_name', 'user__last_name', 'national_id', 'employer')
  list_filter = ('user__date_joined', 'employer')

  def get_phone(self, obj):
    return obj.user.phone
  get_phone.short_description = 'رقم الهاتف'