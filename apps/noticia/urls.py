from django.urls import path
from .views import NoticiaListview

urlpatterns = [
    path('noticias', NoticiaListview.as_view())
]
