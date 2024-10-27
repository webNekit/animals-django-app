from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Report

@admin.register(Report)
class ReportAdmin(ModelAdmin):
    list_display = ['name', 'file', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['name']
    sortable_by = ['created_at']