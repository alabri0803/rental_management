from rest_framework.routers import DefaultRouter
from .views import TenantViewSet, ContractViewSet, PaymentViewSet, UnitViewSet

router = DefaultRouter()
router.register(r'tenants', TenantViewSet)
router.register(r'contracts', ContractViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'units', UnitViewSet)

urlpatterns = router.urls