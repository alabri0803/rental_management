from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import gettext_lazy as _
from .models import Building, Floor, Unit
from .forms import UnitForm

def building_list(request):
  buildings = Building.objects.all()
  return render(request, 'buildings/building_list.html', {'buildings': buildings})

def building_detail(request, pk):
  building = get_object_or_404(Building, pk=pk)
  return render(request, 'buildings/building_detail.html', {'building': building})

def floor_list(request, building_id):
  building = get_object_or_404(Building, pk=building_id)
  floors = building.floors.all()
  return render(request, 'buildings/floor_list.html', {'building': building, 'floors': floors})

def unit_list(request, floor_id):
  floor = get_object_or_404(Floor, pk=floor_id)
  units = floor.units.all()
  return render(request, 'buildings/unit_list.html', {'floor': floor, 'units': units})

def unit_detail(request, pk):
  unit = get_object_or_404(Unit, pk=pk)
  return render(request, 'buildings/unit_detail.html', {'unit': unit})

def unit_create(request):
  if request.method == 'POST':
    form = UnitForm(request.POST)
    if form.is_valid():
      unit = form.save()
      return redirect('buildings:unit_detail', pk=unit.pk)
  else:
    form = UnitForm()
  return render(request, 'buildings/unit_form.html', {'form': form})

def unit_update(request, pk):
  unit = get_object_or_404(Unit, pk=pk)
  if request.method == 'POST':
    form = UnitForm(request.POST, instance=unit)
    if form.is_valid():
      unit = form.save()
      return redirect('buildings:unit_detail', pk=unit.pk)
  else:
    form = UnitForm(instance=unit)
  return render(request, 'buildings/unit_form.html', {'form': form})

def unit_delete(request, pk):
  unit = get_object_or_404(Unit, pk=pk)
  if request.method == 'POST':
    unit.delete()
    return redirect('buildings:building_list')