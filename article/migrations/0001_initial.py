# Generated by Django 5.1.2 on 2024-10-28 17:30

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Например: объявление', max_length=255, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL - ссылка')),
                ('is_active', models.BooleanField(default=True, verbose_name='Отображать на сайте')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Например: Отлов бродячих животных', max_length=255, verbose_name='Название статьи')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL - ссылка')),
                ('small_text', models.TextField(help_text='Например: Законопроект по отлову бродячих животных', verbose_name='Краткое описание')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Контент статьи')),
                ('image', models.ImageField(blank=True, help_text='Загрузите изображение', null=True, upload_to='article/', verbose_name='Изображение')),
                ('is_active', models.BooleanField(default=True, verbose_name='Отображать на сайте')),
                ('is_featured', models.BooleanField(default=False, verbose_name='Отображать на главной странице')),
                ('is_banner', models.BooleanField(default=False, verbose_name='Отображать в баннере')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('category', models.ForeignKey(help_text='Выберите категорию', on_delete=django.db.models.deletion.CASCADE, to='article.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]