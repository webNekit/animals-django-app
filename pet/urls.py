from django.urls import path
from . import views

app_name = "pet"

urlpatterns = [
    path('', views.pets_list, name="pets_list"),
    path('<slug:slug>/', views.pet_detail, name="page_detail"),
]