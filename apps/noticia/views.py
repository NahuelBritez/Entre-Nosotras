from django.shortcuts import render
from django.views.generic import ListView
from .models import Noticia

# Create your views here.

class NoticiaListview(ListView):
    model = Noticia
    template_name = 'noticias.html'