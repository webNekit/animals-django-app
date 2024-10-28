from django.apps import AppConfig


class ArticleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = "Статьи и новости"
    name = 'article'
