from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import SiteSettings, AdditionalPhone, SocialLink, AdditionalEmail

class AdditionalPhoneInline(admin.TabularInline):
    model = AdditionalPhone
    extra = 1

class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1

class AdditionalEmailInline(admin.TabularInline):
    model = AdditionalEmail
    extra = 1

@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    inlines = [AdditionalPhoneInline, SocialLinkInline, AdditionalEmailInline]

    def has_add_permission(self, request):
        # Запрещаем добавление, если запись уже существует
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Запрещаем удаление записи
        return False