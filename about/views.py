from django.shortcuts import render
from .models import Gallery

def index(request):
    galleries = Gallery.objects.all()
    return render(request, "about/page-index.html", {
        'galleries': galleries,
        'title': "О нас",
        'meta_text': "О нас",
        'meta_keywords': "питомцы, помощь питомцам"
    })