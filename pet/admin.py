from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Pet, PetImage, Category, Breed

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'slug', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    list_display_links = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Breed)
class BreedAdmin(ModelAdmin):
    list_display = ('name', 'slug', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    list_display_links = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class PetImageInline(admin.TabularInline):
    model = PetImage
    extra = 2

@admin.register(Pet)
class PetAdmin(ModelAdmin):
    list_display = ('name', 'slug', 'category', 'breed', 'is_active', 'is_featured', 'is_banner')
    list_filter = ('is_active', 'is_featured', 'is_banner', 'category', 'breed')
    list_editable = ('is_active', 'is_featured', 'is_banner', 'category', 'breed')
    list_display_links = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [PetImageInline]