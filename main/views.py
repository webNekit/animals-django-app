from django.shortcuts import render
from reference.models import Reference
from cash.models import Cash
from pet.models import Pet
from article.models import Article

def index(request):
    pets = Pet.objects.filter(is_active=True, is_featured=True).order_by("-created_at").prefetch_related('images')[:6]
    references = Reference.objects.filter(is_active=True, is_featured=True).order_by("-created_at")[:3]
    articles = Article.objects.filter(is_active=True, is_featured=True).order_by("-created_at")[:3]
    cashs = Cash.objects.filter(is_active=True, is_accent=True)[:3]
    #to Banner
    petsBanner = Pet.objects.filter(is_active=True, is_banner=True).order_by("-created_at").prefetch_related('images')
    referencesBanner = Reference.objects.filter(is_active=True, is_banner=True).order_by("-created_at")
    articlesBanner = Article.objects.filter(is_active=True, is_banner=True).order_by("-created_at")
    return render(request, "main/page-index.html", {
        'references': references,
        'cashs': cashs,
        'pets': pets,
        'articles': articles,
        'petsBanner': petsBanner,
        'referencesBanner': referencesBanner,
        'articlesBanner': articlesBanner,
        'title': 'Главная',
        'meta_text': 'Помощь животным',
        'meta_keywords': 'питомцы, помощь питомцам'
    })

