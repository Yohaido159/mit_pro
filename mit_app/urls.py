from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import MitnadvCreateView,MitnadvDetailView, SnifDetailView, MitnadviListView, SnifListView, SnifCreateView


urlpatterns = [
    path("mit/<int:pk>",MitnadvDetailView.as_view(), name = "mitnadv-detail"),
    path("mit/list",MitnadviListView.as_view(), name = "mitnadvim-list"),
    path("mit/add",MitnadvCreateView.as_view(), name = "mitnadv-create"),
    
    path("snif/<int:pk>",SnifDetailView.as_view(), name = "snif-detail"),
    path("snif/list",SnifListView.as_view(), name = "snifs-list"),
    path("snif/add",SnifCreateView.as_view(), name = "snif-create"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
