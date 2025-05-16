from django.urls import path
from . import views

app_name = 'tenants'

urlpatterns = [
  path('', views.tenant_list, name='list'),
  path('add/', views.tenant_create, name='add'),
  path('<int:pk>/', views.tenant_detail, name='detail'),
  path('<int:pk>/edit/', views.tenant_update, name='edit'),
]