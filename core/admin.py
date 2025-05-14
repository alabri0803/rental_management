from django.contrib import admin
from django.utils.formats import date_format

def format_arabic_date(obj):
  return date_format(obj.date, "DATE_FORMAT")
format_arabic_date.short_description = "تاريخ الدفع"