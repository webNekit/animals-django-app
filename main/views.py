from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from .utils import send_message_to_telegram
from reference.models import Reference
from cash.models import Cash
from pet.models import Pet
from article.models import Article
from about.models import Gallery

def index(request):
    pets = Pet.objects.filter(is_active=True, is_featured=True).order_by("-created_at").prefetch_related('images')[:6]
    references = Reference.objects.filter(is_active=True, is_featured=True).order_by("-created_at")[:3]
    articles = Article.objects.filter(is_active=True, is_featured=True).order_by("-created_at")[:3]
    cashs = Cash.objects.filter(is_active=True, is_accent=True)[:3]
    galleries = Gallery.objects.filter(is_featured=True)[:6]
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
        'galleries': galleries,
        'referencesBanner': referencesBanner,
        'articlesBanner': articlesBanner,
        'title': 'Главная',
        'meta_text': 'объединить неравнодушных людей для помощи животным, оказавшимся в трудной ситуации. Мы верим, что совместными усилиями сможем сделать мир добрее и безопаснее для всех живых существ. На нашем сайте вы найдете информацию о том, как помочь нуждающимся питомцам, станете частью активного сообщества, узнаете о важных акциях и событиях. Присоединяйтесь, чтобы внести свой вклад в заботу о наших меньших братьях.',
        'meta_keywords': 'помощь животным, защита животных, приюты для животных, забота о животных, спасение животных, благотворительность для животных'
    })

def contacts(request):
    return render(request, "main/page-contact.html", {
        'title': 'Контакты',
        'meta_text': 'Контакты',
        'meta_keywords': 'питомцы, помощь питомцам'
    })


def submit_application(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        message = f"Новая заявка на обратную связь:\nИмя: {first_name}\nФамилия: {last_name}\nТелефон: {phone}\nEmail: {email}"


        send_message_to_telegram(message)
        return JsonResponse({'success': True})

    return JsonResponse({'success': False})