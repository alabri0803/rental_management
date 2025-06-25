from django.urls import path

from . import views

app_name = 'properties'

urlpatterns = [
  # قائمة العقارات
  path('', views.property_list, name='property_list'),
  path('my-properties/', views.my_properties, name='my_properties'),
  # تفاصيل العقار
  path('<int:property_id>/', views.property_detail, name='property_detail'),
  # إضافة وتعديل العقارات
  path('add/', views.property_add, name='property_add'),
  path('<int:property_id>/edit/', views.property_edit, name='property_edit'),
  path('<int:property_id>/delete/', views.property_delete, name='property_delete'),
  # إدارة صور العقار
  path('<int:pk>/images/', views.property_images, name='property_images'),
  path('<int:pk>/images/add/', views.add_property_image, name='add_property_image'),
  path('images/<int:image_id>/delete/', views.delete_property_image, name='delete_property_image'),
  # البحث والتصفية
  path('search/', views.property_search, name='property_search'),
]