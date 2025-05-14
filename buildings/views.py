from django.shortcuts import render, redirect, get_object_or_404
from .models import Unit
from .forms import UnitForm

def unit_list(request):
  units = Unit.objects.all()
  return render(request, 'buildings/unit_list.html', {'units': units})

def unit_detail(request, pk):
  unit = get_object_or_404(Unit, pk=pk)
  return render(request, 'buildings/unit_detail.html', {'unit': unit})

def unit_create(request):
  form = UnitForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('unit_list')
  return render(request, 'buildings/unit_form.html', {'form': form})

def unit_update(request, pk):
  unit = get_object_or_404(Unit, pk=pk)
  form = UnitForm(request.POST or None, instance=unit)
  if form.is_valid():
    form.save()
    return redirect('unit_list', pk=unit.pk)
  return render(request, 'buildings/unit_form.html', {'form': form})