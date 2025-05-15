from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
  path('summary/', views.summary_report, name='summary_report'),
  path('occupancy/', views.occupancy_report, name='occupancy_report'),
  path('revenue/', views.revenue_report, name='revenue_report'),
]