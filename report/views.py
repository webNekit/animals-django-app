from django.shortcuts import render
from .models import Report

# Create your views here.
def report_list(request):
    reports = Report.objects.filter(is_active=True)
    return render(request, "report/page-index.html", {
        'reports': reports,
        'title': 'Отчеты',  
    })