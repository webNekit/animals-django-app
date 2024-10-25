from django.shortcuts import render
from .models import Cash

def cash_list(request):
    cash = Cash.objects.all()
    return render(request, "cash/page-index.html", {
        'cash': cash
    })