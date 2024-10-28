from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории", help_text="Например: объявление")
    slug = models.SlugField(max_length=255, verbose_name="URL - ссылка", unique=True)
    is_active = models.BooleanField(default=True, verbose_name="Отображать на сайте")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
    
class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", help_text="Выберите категорию")
    title = models.CharField(max_length=255, verbose_name="Название статьи", help_text="Например: Отлов бродячих животных")
    slug = models.SlugField(max_length=255, verbose_name="URL - ссылка", unique=True)
    small_text = models.TextField(verbose_name="Краткое описание", help_text="Например: Законопроект по отлову бродячих животных", blank=False)
    content = RichTextField(verbose_name="Контент статьи", blank=False)
    image = models.ImageField(upload_to="article/", verbose_name="Изображение", help_text="Загрузите изображение", blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="Отображать на сайте")
    is_featured = models.BooleanField(default=False, verbose_name="Отображать на главной странице")
    is_banner = models.BooleanField(default=False, verbose_name="Отображать в баннере")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title