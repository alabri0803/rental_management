from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from django.contrib import messages
from .models import Building, Floor, Unit, Governorate, Wilayat
from .forms import UnitForm, BuildingFilterForm
from .filters import BuildingFilter

class BuildingListView(FilterView):
  model = Building
  template_name = 'buildings/building_list.html'
  context_object_name = 'buildings'
  filterset_class = BuildingFilter
  paginate_by = 10

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['governorates'] = Governorate.objects.filter(is_active=True)
    context['filter_form'] = BuildingFilterForm(self.request.GET or None)
    return context

class BuildingDetailView(DetailView):
  model = Building
  template_name = 'buildings/building_detail.html'
  context_object_name = 'building'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['floors'] = self.object.floors.all().order_by('number')
    return context

class FloorListView(ListView):
  model = Floor
  template_name = 'buildings/floor_list.html'
  context_object_name = 'floors'

  def get_queryset(self):
    building = get_object_or_404(Building, pk=self.kwargs['building_id'])
    return building.floors.all().order_by('number')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['building'] = self.building
    return context

class UnitListView(ListView):
  model = Unit
  template_name = 'buildings/unit_list.html'
  context_object_name = 'units'
  paginate_by = 10

  def get_queryset(self):
    floor = get_object_or_404(Floor, pk=self.kwargs['floor_id'])
    return self.floor.units.all().order_by('unit_number')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['floor'] = self.floor
    return context

class UnitDetailView(DetailView):
  model = Unit
  template_name = 'buildings/unit_detail.html'
  context_object_name = 'unit'

class UnitCreateView(LoginRequiredMixin, CreateView):
  model = Unit
  form_class = UnitForm
  template_name = 'buildings/unit_form.html'
  success_url = reverse_lazy('buildings:building_list')

  def get_initial(self):
    initial = super().get_initial()
    if 'floor_id' in self.kwargs:
      initial['floor'] = get_object_or_404(Floor, pk=self.kwargs['floor_id'])
    return initial

  def form_valid(self, form):
    messages.success(self.request, _("تم إضافة الوحدة بنجاح."))
    return super().form_valid(form)

class UnitUpdateView(LoginRequiredMixin, UpdateView):
  model = Unit
  form_class = UnitForm
  template_name = 'buildings/unit_form.html'

  def get_success_url(self):
    return reverse_lazy('buildings:unit_detail', kwargs={'pk': self.object.pk})

  def form_valid(self, form):
    messages.success(self.request, _("تم تحديث بيانات الوحدة بنجاح."))
    return super().form_valid(form)

class UnitDeleteView(LoginRequiredMixin, DeleteView):
  model = Unit
  template_name = 'buildings/unit_confirm_delete.html'
  success_url = reverse_lazy('buildings:building_list')

  def delete(self, request, *args, **kwargs):
    messages.success(self.request, _("تم حذف الوحدة بنجاح."))
    return super().delete(request, *args, **kwargs)

def load_wilayat(request):
  governorate_id = request.GET.get('governorate')
  wilayat = Wilayat.objects.filter(governorate_id=governorate_id, is_active=True).order_by('name')
  return render(request, 'buildings/wilayat_dropdown_list.html', {'wilayat': wilayat})