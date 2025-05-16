from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TenantViewSet, UnitViewSet, ContractViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'tenants', TenantViewSet)
router.register(r'units', UnitViewSet)
router.register(r'contracts', ContractViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
  path('', include(router.urls))
]