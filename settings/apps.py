from django.apps import AppConfig


class SettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = "Информация на сайте"
    name = 'settings'
