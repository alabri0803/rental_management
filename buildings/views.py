from django.shortcuts import render, get_object_or_404, redirect
from .models import Building, Unit
from .forms import UnitForm

def floor_list(request):
  buildings = Building.objects.all()
  return render(request, 'buildings/floor_list.html', {'buildings': buildings})

def unit_list(request):
  units = Unit.objects.select_related('building').all()
  return render(request, 'buildings/unit_list.html', {'units': units})

def unit_detail(request, pk):
  unit = get_object_or_404(Unit, pk=pk)
  return render(request, 'buildings/unit_detail.html', {'unit': unit})

def unit_form(request):
  if request.method == 'POST':
    form = UnitForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('buildings:unit_list')
  else:
    form = UnitForm()
  return render(request, 'buildings/unit_form.html', {'form': form})