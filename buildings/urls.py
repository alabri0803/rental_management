from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views

app_name = 'buildings'

urlpatterns = [
  path('', views.BuildingListView.as_view(), name='building_list'),
  path(_('<int:pk>/'), views.BuildingDetailView.as_view(), name='building_detail'),

  path(_('<int:building_id>/floors/'), views.FloorListView.as_view(), name='floor_list'),
  path(_('floors/<int:floor_id>/units/'), views.UnitListView.as_view(), name='unit_list'),

  path(_('units/<int:pk>/'), views.UnitDetailView.as_view(), name='unit_detail'),
  path(_('units/new/'), views.UnitCreateView.as_view(), name='unit_create'),
  path(_('units/<int:pk>/edit/'), views.UnitUpdateView.as_view(), name='unit_update'),
  path(_('units/<int:pk>/delete/'), views.UnitDeleteView.as_view(), name='unit_delete'),

  path('ajax/load-wilayat/', views.load_wilayat, name='ajax_load_wilayat'),
]