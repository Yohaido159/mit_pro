from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import MitnadvCreateView,MitnadvDetailView, SnifDetailView


urlpatterns = [
    path("mit/add",MitnadvCreateView.as_view(), name = "mitnadv-create"),
    path("mit/<int:pk>",MitnadvDetailView.as_view(), name = "mitnadv-detail"),
    path("snif/<int:pk>",SnifDetailView.as_view(), name = "snif-detail"),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
