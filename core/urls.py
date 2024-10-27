from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cash/', include('cash.urls', namespace='cash')),
    path('report/', include('report.urls', namespace='report')),
    path('reference/', include('reference.urls', namespace='reference')),
    path('pet/', include('pet.urls', namespace='pet')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)