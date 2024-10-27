from django.apps import AppConfig


class PetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = "Питомцы"
    name = 'pet'
