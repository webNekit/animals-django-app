from django.shortcuts import render
from .models import Reference

def reference_list(request):
    references = Reference.objects.filter(is_active=True)
    return render(request, "reference/page-index.html", {
        'references': references,
        'title': 'Справочники',
    })

def reference_detail(request, slug):
    reference = Reference.objects.get(slug=slug)
    return render(request, "reference/page-detail.html", {
        'reference': reference,
    })