from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
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
    return redirect(reverse_lazy('buildings:list'))
  return render(request, 'buildings/unit_form.html', {'form': form})

def unit_update(request, pk):
  unit = get_object_or_404(Unit, pk=pk)
  form = UnitForm(request.POST or None, instance=unit)
  if form.is_valid():
    form.save()
    return redirect(reverse_lazy('buildings:detail', kwargs={'pk': pk}))
  return render(request, 'buildings/unit_form.html', {'form': form})

def floor_list(request):
  floors = Floor.objects.prefetch_related('units').all()
  return render(request, 'buildings/floor_list.html', {'floors': floors})