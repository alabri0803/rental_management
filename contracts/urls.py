from django.urls import path
from . import views

urlpatterns = [
  path('', views.contract_list, name='contract_list'),
  path('add/', views.contract_create, name='contract_create'),
  path('<int:pk>/', views.contract_detail, name='contract_detail'),
  path('<int:pk>/edit/', views.contract_update, name='contract_update'),
  #path('<int:pk>/pdf/', views.contract_pdf, name='contract_pdf'),
  #path('<int:pk>/email/', views.contract_email, name='contract_email'),
]