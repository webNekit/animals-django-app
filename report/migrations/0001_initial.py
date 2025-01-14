# Generated by Django 5.1.2 on 2024-10-25 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Например: отчет по закупкам лекарств', max_length=255, verbose_name='Название фин.отчета')),
                ('file', models.FileField(help_text='Загрузите файл отчета', upload_to='reports/', verbose_name='Файл отчета')),
                ('is_active', models.BooleanField(default=True, verbose_name='Отображать на сайте')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата формирования отчета')),
            ],
            options={
                'verbose_name': 'Отчет',
                'verbose_name_plural': 'Отчет',
            },
        ),
    ]
