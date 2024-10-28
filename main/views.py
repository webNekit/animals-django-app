from django.shortcuts import render
from reference.models import Reference
from cash.models import Cash
from pet.models import Pet

def index(request):
    pets = Pet.objects.filter(is_active=True, is_featured=True).order_by("-created_at").prefetch_related('images')[:6]
    references = Reference.objects.filter(is_active=True, is_featured=True).order_by("-created_at")[:3]
    cashs = Cash.objects.filter(is_active=True, is_accent=True)[:3]
    return render(request, "main/page-index.html", {
        'references': references,
        'cashs': cashs,
        'pets': pets,
        'title': 'Главная',
        'meta_text': 'Помощь животным',
        'meta_keywords': 'питомцы, помощь питомцам'
    })