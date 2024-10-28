from django.db import models

class SiteSettings(models.Model):
    site_name = models.CharField("Название сайта", max_length=100)
    main_phone = models.CharField("Основной номер телефона", help_text="Например: 78885554433", max_length=20, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.pk = 1  # Устанавливаем фиксированный первичный ключ
        super().save(*args, **kwargs)

    @classmethod
    def get_instance(cls):
        # Получаем или создаем единственную запись
        instance, created = cls.objects.get_or_create(pk=1)
        return instance

    def __str__(self):
        return "Настройки сайта"

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"


class AdditionalPhone(models.Model):
    settings = models.ForeignKey(SiteSettings, related_name="additional_phones", on_delete=models.CASCADE)
    phone = models.CharField("Доп. номер телефона", max_length=20)

    class Meta:
        verbose_name = "доп. номер телефона"
        verbose_name_plural = "Доп. номера телефонов"

    def __str__(self):
        return self.phone


class SocialLink(models.Model):
    settings = models.ForeignKey(SiteSettings, related_name="social_links", on_delete=models.CASCADE)
    icon = models.ImageField("Иконка соц. сети", upload_to="social_icons/")
    url = models.URLField("Ссылка на соц. сеть")

    class Meta:
        verbose_name = "соц.сеть"
        verbose_name_plural = "соц.сети"

    def __str__(self):
        return self.url


class AdditionalEmail(models.Model):
    settings = models.ForeignKey(SiteSettings, related_name="additional_emails", on_delete=models.CASCADE)
    email = models.EmailField("Доп. email")

    class Meta:
        verbose_name = "email"
        verbose_name_plural = "email"

    def __str__(self):
        return self.email
