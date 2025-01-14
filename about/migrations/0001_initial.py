# Generated by Django 5.1.2 on 2024-10-29 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Загрузите изображение', upload_to='about/gallery', verbose_name='Изображение')),
                ('is_featured', models.BooleanField(default=False, verbose_name='Отображать на главной странице')),
            ],
            options={
                'verbose_name': 'изображение для раздела о нас',
                'verbose_name_plural': 'Изображения для раздела о нас',
            },
        ),
    ]
