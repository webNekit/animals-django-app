from django.shortcuts import render, get_object_or_404
from .models import Pet

def pets_list(request):
    pets = Pet.objects.filter(is_active=True).prefetch_related('images')
    return render(request, "pet/page-index.html", {
        "title": "Питомцы",
        "meta_text": "Список питомцев",
        "meta_keywords": "питомцы, помощь питомцам",
        "pets": pets
    })

def pet_detail(request, slug):
    pet = get_object_or_404(Pet, slug=slug, is_active=True)
    return render(request, "pet/page-detail.html", {
        'pet': pet,
        'title': pet.meta_title,
        'meta_text': pet.meta_text,
        'meta_keywords': pet.meta_keywords
    })