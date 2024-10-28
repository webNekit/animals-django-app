from django.shortcuts import render, get_object_or_404
from .models import Article, Category


def article_list(request):
    articles = Article.objects.filter(is_active=True).order_by("-created_at")
    return render(request, "article/page-index.html", {
        "title": "Статьи",
        "meta_text": "Список статей",
        "meta_keywords": "статьи, новости",
        "articles": articles
    })

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, is_active=True)
    return render(request, "article/page-detail.html", {
        'article': article,
        'title': article.title,
        'meta_text': article.small_text,
        'meta_keywords': article.small_text
    })