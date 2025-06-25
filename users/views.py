from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import redirect, render

from contracts.models import Contract
from properties.models import Property

from .forms import CustomUserCreationForm, OwnerForm, TenantForm, UserProfileForm
from .models import Owner, Tenant


def home(request):
  """الصفحة الرئيسية"""
  context = {
    'total_properties': Property.objects.count(),
    'total_contracts': Contract.objects.count(),
    'active_contracts': Contract.objects.filter(status='active').count(),
    'total_owners': Owner.objects.count(),
    'total_tenants': Tenant.objects.count(),
  }
  if request.user.is_authenticated:
    # إحصائيات للمستخدمين المسجل
    if hasattr(request.user, 'owner'):
      context['user_properties'] = Property.objects.filter(owner=request.user.owner).count()
      context['user_contracts'] = Contract.objects.filter(owner=request.user.owner).count()
    elif hasattr(request.user, 'tenant'):
      context['user_contracts'] = Contract.objects.filter(tenant=request.user.tenant).count()
    return render(request, 'users/home.html', context)

def register_owner(request):
  """تسجيل مالك جديد"""
  if request.method == 'POST':
    user_form = CustomUserCreationForm(request.POST)
    owner_form = OwnerForm(request.POST, request.FILES)
    if user_form.is_valid() and owner_form.is_valid():
      user = user_form.save()
      owner = owner_form.save(commit=False)
      owner.user = user
      owner.save()
      login(request, user)
      messages.success(request, 'تم تسجيل حسابك كمالك بنجاح!')
      return redirect('home')
  else:
    user_form = CustomUserCreationForm()
    owner_form = OwnerForm()
    context = {
      'user_form': user_form,
      'owner_form': owner_form,
      'user_type': 'owner'
    }
    return render(request, 'users/register.html', context)

def register_tenant(request):
  """تسجيل مستأجر جديد"""
  if request.method == 'POST':
    user_form = CustomUserCreationForm(request.POST)
    tenant_form = TenantForm(request.POST, request.FILES)
    if user_form.is_valid() and tenant_form.is_valid():
      user = user_form.save()
      tenant = tenant_form.save(commit=False)
      tenant.user = user
      tenant.save()
      login(request, user)
      messages.success(request, 'تم تسجيل حسابك كمستأجر بنجاح!')
      return redirect('home')
  else:
    user_form = CustomUserCreationForm()
    tenant_form = TenantForm()
    context = {
      'user_form': user_form,
      'tenant_form': tenant_form,
      'user_type': 'tenant'
    }
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
  """ملف المستخدم"""
  if request.method == 'POST':
    form = UserProfileForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      messages.success(request, 'تم تحديث ملفك الشخصي بنجاح!')
      return redirect('profile')
  else:
    form = UserProfileForm(instance=request.user)
    context = {
      'form': form,
      'user_type': 'owner' if hasattr(request.user, 'owner') else 'tenant' if hasattr(request.user, 'tenant') else 'user'
    }
    return render(request, 'users/profile.html', context)

@login_required
def dashboard(request):
  """لوحة التحكم"""
  context = {}
  if hasattr(request.user, 'owner'):
    # لوحة التحكم للمالك
    owner = request.user.owner
    properties = Property.objects.filter(owner=owner)
    contracts = Contract.objects.filter(owner=owner)
    context.update({
      'user_type': 'owner',
      'properties': properties,
      'total_properties': properties.count(),
      'available_properties': properties.filter(is_available=True).count(),
      'total_contracts': contracts.count(),
      'active_contracts': contracts.filter(status='active').count(),
      'expiring_contracts': contracts.filter(status='expiring_soon').count(),
      'recent_contracts': contracts.order_by('-created_at')[:5],
      'monthly_income': contracts.filter(status='active').aggregate(Sum('monthly_rent'))['total'] or 0,
    })
  elif hasattr(request.user, 'tenant'):
    # لوحة التحكم للمستأجر
    tenant = request.user.tenant
    contracts = Contract.objects.filter(tenant=tenant)
    context.update({
      'user_type': 'tenant',
      'total_contracts': contracts.count(),
      'active_contracts': contracts.filter(status='active').count(),
      'recent_contracts': contracts.order_by('-created_at')[:5],
      'current_rent': contracts.filter(status='active').aggregate(Sum('monthly_rent'))['total'] or 0,
    })
    return render(request, 'users/dashboard.html', context)