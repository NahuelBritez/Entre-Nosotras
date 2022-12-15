from django.shortcuts import render
from apps.noticia.models import Noticia
from django.views.generic import ListView

class NoticiaListview(ListView):
    model = Noticia
    template_name = 'index.html'

def noticias(request):
    return render(request,'noticias.html')