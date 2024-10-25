from django.urls import path
from . import views

app_name = "cash"

urlpatterns = [
    path('', views.cash_list, name='cash_list'),
]