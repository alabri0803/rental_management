from django.test import TestCase
from tenants.models import Tenant

class TenantModelTest(TestCase):
  def setUp(self):
    self.tenant = Tenant.objects.create(
      full_name="أحمد العامري",
      national_id="1234567890",
      phone="99999999",
      email="ahmed@example.com",
    )

  def test_tenant_creation(self):
    self.assertEqual(self.tenant.full_name, "أحمد العامري")
    self.assertEqual(self.tenant.status, 'AC')