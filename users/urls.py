from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
  # الصفحة الرئيسية
  path('', views.home, name='home'),
  # التسجيل
  path('register/owner/', views.register_owner, name='register_owner'),
  path('register/tenant/', views.register_tenant, name='register_tenant'),
  # تسجيل الدخول والخروج
  path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  # الملف الشخصي ولوحة التحكم
  path('profile/', views.profile, name='profile'),
  path('dashboard/', views.dashboard, name='dashboard'),
  # إعادة تعيين كلمة المرور
  path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
  path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
  path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
  path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]