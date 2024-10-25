from django.urls import path
from . import views

app_name = "report"

urlpatterns = [
    path('', views.report_list, name='report_list'),
]