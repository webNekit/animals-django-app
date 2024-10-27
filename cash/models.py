from django.db import models

class Cash(models.Model):
    number = models.BigIntegerField(verbose_name="Номер карты", help_text="Укажите код карты получателя")
    bank = models.CharField(max_length=255, verbose_name="Название банка", help_text="Укажите название банка получателя")
    owner = models.CharField(max_length=255, verbose_name="Получатель", help_text="Укажите ФИО получателя")
    is_accent = models.BooleanField(default=False, verbose_name="Отображать на главной странице")
    is_active = models.BooleanField(default=True, verbose_name="Отображать на сайте")

    class Meta:
        verbose_name = "Реквизит"
        verbose_name_plural = "Список реквизитов"

    def __str__(self) -> str:
        return f"{self.owner} - {self.bank}"