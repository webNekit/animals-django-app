from django.shortcuts import render
from .models import Cash

def cash_list(request):
    cash = Cash.objects.filter(is_active=True)
    return render(request, "cash/page-index.html", {
        'title': "Реквизиты",
        'cashs': cash,
    })