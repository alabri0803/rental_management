from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
  path('', views.payment_list, name='payment_list'),
  path('add/', views.payment_create, name='payment_create'),
  path('<int:pk>/', views.payment_detail, name='payment_detail'),
  path('<int:pk>/edit/', views.payment_update, name='payment_update'),
]