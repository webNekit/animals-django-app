from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории", help_text="Укажите название категории")
    slug = models.SlugField(max_length=255, verbose_name="URL - ссылка", unique=True)
    is_active = models.BooleanField(default=True, verbose_name="Отображать на сайте")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Категория питомцев"
        verbose_name_plural = "Категории питомцев"

    def __str__(self) -> str:
        return self.name
    
class Breed(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название породы", help_text="Укажите название породы")
    slug = models.SlugField(max_length=255, verbose_name="URL - ссылка", unique=True)
    is_active = models.BooleanField(default=True, verbose_name="Отображать на сайте")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Порода питомцев"
        verbose_name_plural = "Породы питомцев"

    def __str__(self) -> str:
        return self.name
    
class Pet(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория питомца", help_text="Выберите категорию питомца")
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name="Порода питомца", help_text="Выберите породу питомца")
    name = models.CharField(max_length=255, verbose_name="Кличка питомца", help_text="Например: Кузя")
    slug = models.SlugField(max_length=255, verbose_name="URL - ссылка", unique=True)
    age = models.CharField(max_length=255, verbose_name="Возраст питомца", help_text="Например: 2 года 8 месяцев")
    contact = models.CharField(max_length=255, verbose_name="Контактный номер телефона", help_text="Например: +7 999 999 99 99", blank=False)
    content = RichTextField(verbose_name="Описание", help_text="Например: Кузя добрый и послушный мальчик, который ищет дом...", blank=False)
    is_active = models.BooleanField(default=True, verbose_name="Отображать на сайте")
    is_featured = models.BooleanField(default=False, verbose_name="Отображать на главной странице")
    is_banner = models.BooleanField(default=False, verbose_name="Отображать в баннере")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    #meta-полля
    meta_title = models.CharField(max_length=255, verbose_name="Мета-заголовок", help_text="Укажите мета-заголовок", blank=True)
    meta_text = models.TextField(verbose_name="Мета-описание", help_text="Укажите мета-описание", blank=True)
    meta_keywords = models.CharField(max_length=255, verbose_name="Ключевые слова", help_text="Укажите ключевые слова", blank=True)
    class Meta:
        verbose_name = "Питомец"
        verbose_name_plural = "Питомцы"

    def __str__(self) -> str:
        return self.name
    
class PetImage(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="images", verbose_name="Питомец")
    image = models.ImageField(upload_to="pets/", verbose_name="Изображение", help_text="Загрузите изображение")

    class Meta:
        verbose_name = "изображение для питомца"
        verbose_name_plural = "Изображения для питомца"

    def __str__(self) -> str:
        return f"Изображение для {self.pet.name}"