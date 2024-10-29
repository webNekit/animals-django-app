from django.contrib import admin
from unfold.admin import ModelAdmin
from django.utils.html import format_html
from .models import Gallery

@admin.register(Gallery)
class GalleryAdmin(ModelAdmin):
    list_display = ['image_tag', 'is_featured']
    list_editable = ['is_featured']
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="74" height="74" style="border-radius: 7px;" />'.format(obj.image.url))
        return None
    image_tag.short_description = "Изображение"
