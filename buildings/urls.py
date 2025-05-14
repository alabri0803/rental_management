from django.urls import path
from . import views

urlpatterns = [
  path('', views.unit_list, name='unit_list'),
  path('add/', views.unit_create, name='unit_create'),
  path('<int:pk>/', views.unit_detail, name='unit_detail'),
  path('<int:pk>/edit/', views.unit_update, name='unit_update'),
]