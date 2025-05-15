from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Tenant
from .forms import TenantForm

def tenant_list(request):
  tenants = Tenant.objects.all()
  return render(request, 'tenants/tenant_list.html', {'tenants': tenants})

def tenant_detail(request, pk):
  tenant = get_object_or_404(Tenant, pk=pk)
  return render(request, 'tenants/tenant_detail.html', {'tenant': tenant})

def tenant_create(request):
  form = TenantForm(request.POST or None, request.FILES or None)
  if form.is_valid():
    form.save()
    return redirect(reverse_lazy('tenants:list'))
  return render(request, 'tenants/tenant_form.html', {'form': form})

def tenant_update(request, pk):
  tenant = get_object_or_404(Tenant, pk=pk)
  form = TenantForm(request.POST or None, request.FILES or None, instance=tenant)
  if form.is_valid():
    form.save()
    return redirect(reverse_lazy('tenants:detail', kwargs={'pk': pk}))
  return render(request, 'tenants/tenant_form.html', {'form': form})