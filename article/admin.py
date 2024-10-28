from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Article, Category

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'slug', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    list_display_links = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = ('title', 'category', 'is_active', 'is_featured', 'is_banner')
    list_filter = ('is_active', 'is_featured', 'is_banner', 'category')
    list_editable = ('is_active', 'is_featured', 'is_banner', 'category')
    list_display_links = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}