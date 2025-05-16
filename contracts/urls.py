from django.urls import path
from . import views

app_name = 'contracts'

urlpatterns = [
  path('', views.contract_list, name='list'),
  path('add/', views.contract_create, name='add'),
  path('<int:pk>/', views.contract_detail, name='detail'),
  path('<int:pk>/edit/', views.contract_update, name='edit'),
]