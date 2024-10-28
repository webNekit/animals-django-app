from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Cash

@admin.register(Cash)
class CashAdmin(ModelAdmin):
    list_display = ('number', 'owner', 'is_accent', 'is_active')
    list_filter = ('number', 'owner', 'is_accent', 'is_active')
    list_editable = ('is_accent', 'is_active')
    search_fields = ('number', 'owner')