from django.db import models

class Gallery(models.Model):
    image = models.ImageField(upload_to="about/gallery", verbose_name="Изображение", help_text="Загрузите изображение")
    is_featured = models.BooleanField(default=False, verbose_name="Отображать на главной странице")

    class Meta:
        verbose_name = "изображение для раздела о нас"
        verbose_name_plural = "Изображения для раздела о нас"

    def __str__(self):
        return self.image.url