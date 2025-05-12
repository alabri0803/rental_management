from django.urls import path
from . import views

app_name = 'buildings'

urlpatterns = [
  path('', views.floor_list, name='floor_list'),
  path('units/', views.unit_list, name='unit_list'),
  path('unit/<int:pk>/', views.unit_detail, name='unit_detail'),
  path('unit/add/', views.unit_form, name='unit_form'),
]