from django.urls import path
from . import views

app_name = "reference"

urlpatterns = [
    path('', views.reference_list, name='reference_list'),
    path('<slug:slug>/', views.reference_detail, name='page_detail'),
]