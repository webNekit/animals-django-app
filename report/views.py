from django.shortcuts import render
from .models import Report

# Create your views here.
def report_list(request):
    report = Report.objects.all()
    return render(request, "report/page-index.html", {
        'report': report
    })