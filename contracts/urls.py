from django.urls import path

from . import views

app_name = 'contracts'

urlpatterns = [
  # قائمة العقود
  path('', views.contract_list, name='contract_list'),
  path('my-contracts/', views.my_contracts, name='my_contracts'),
  # تفاصيل العقد
  path('<int:pk>/', views.contract_detail, name='contract_detail'),
  # إضافة وتعديل العقود
  path('add/', views.contract_add, name='contract_add'),
  path('<int:pk>/edit/', views.contract_edit, name='contract_edit'),
  path('<int:pk>/delete/', views.contract_delete, name='contract_delete'),
  # إدارة المدفوعات
  path('<int:pk>/payments/', views.contract_payments, name='contract_payments'),
  path('<int:pk>/payments/add/', views.add_payment, name='add_payment'),
  path('payments/<int:payment_id>/delete/', views.delete_payment, name='delete_payment'),
  # إدارة المستندات
  path('<int:pk>/documents/', views.contract_documents, name='contract_documents'),
  path('<int:pk>/documents/add/', views.add_document, name='add_document'),
  path('documents/<int:document_id>/delete/', views.delete_document, name='delete_document'),
  # إلغاء العقد
  path('<int:pk>/cancel/', views.cancel_contract, name='cancel_contract'),
  path('<int:pk>/cancellation', views.contract_cancellation, name='contract_cancellation'),
  # تجديد العقد
  path('<int:pk>/renew/', views.renew_contract, name='renew_contract'),
  # تعهد سداد المرافق
  path('<int:pk>/utility-commitment/', views.utility_commitment, name='utility_commitment'),
  # النماذج القانونية
  path('<int:pk>/cancellation-form/', views.cancellation_form_pdf, name='cancellation_form_pdf'),
  path('<int:pk>/commitment-form/', views.commitment_form_pdf, name='commitment_form_pdf'),
  path('<int:pk>/contract-form/', views.contract_form_pdf, name='contract_form_pdf'),
  # البحث والتصفية
  path('search/', views.contract_search, name='contract_search'),
  # التقارير
  path('reports/', views.contract_reports, name='contract_reports'),
  path('reports/fees/', views.fees_report, name='fees_report'),
]