from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from .models import Reference

@admin.register(Reference)
class ReferenceAdmin(ModelAdmin):
    list_display = ['title', 'image_tag', 'is_active', 'is_banner', 'is_featured', 'created_at']
    list_editable = ['is_active', 'is_banner', 'is_featured']
    list_filter = ['is_active', 'is_banner', 'is_featured']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="74" height="74" style="border-radius: 7px;" />'.format(obj.image.url))
        return None
    image_tag.short_description = "Изображение"

