from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views

app_name = 'buildings'

urlpatterns = [
  path('', views.building_list, name='building_list'),
  path(_('<int:pk>/'), views.building_detail, name='building_detail'),
  path(_('<int:building_id>/floors/'), views.floor_list, name='floor_list'),
  path(_('floors/<int:floor_id>/units/'), views.unit_list, name='unit_list'),
  path(_('units/<int:unit_id>/'), views.unit_detail, name='unit_detail'),
  path(_('units/new/'), views.unit_create, name='unit_create'),
  path(_('units/<int:pk>/edit/'), views.unit_update, name='unit_update'),
  path(_('units/<int:pk>/delete/'), views.unit_delete, name='unit_delete'),
]