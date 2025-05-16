from django.urls import path
from . import views

app_name = 'buildings'

urlpatterns = [
  path('', views.unit_list, name='list'),
  path('add/', views.unit_create, name='add'),
  path('<int:pk>/', views.unit_detail, name='detail'),
  path('<int:pk>/edit/', views.unit_update, name='edit'),
]