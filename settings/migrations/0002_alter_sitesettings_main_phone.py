# Generated by Django 5.1.2 on 2024-10-29 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='main_phone',
            field=models.CharField(blank=True, help_text='Например: 78885554433', max_length=20, null=True, verbose_name='Основной номер телефона'),
        ),
    ]