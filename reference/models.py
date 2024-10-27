from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Reference(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название записи", help_text="Например: Что делать при отравлении", blank=False)
    slug = models.SlugField(max_length=255, verbose_name="URL - ссылка", unique=True)
    small_text = models.TextField(verbose_name="Краткое описание", help_text="Например: Какие препараты нужны при отравлении? Что делать при отравлении?", blank=False)
    long_text = RichTextField(verbose_name="Описание", help_text="Например: Какие препараты нужны при отравлении? Что делать при отравлении?", blank=False)
    image = models.ImageField(upload_to="reference/", verbose_name="Изображение", help_text="Загрузите изображение", blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="Отображать на сайте")
    is_banner = models.BooleanField(default=False, verbose_name="Отображать в баннере")
    is_featured = models.BooleanField(default=False, verbose_name="Отображать на главной странице")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Справочник"
        verbose_name_plural = "Справочники"

    def __str__(self) -> str:
        return self.title