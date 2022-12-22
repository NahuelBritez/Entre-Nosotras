from django.shortcuts import render,redirect,get_object_or_404
from apps.noticia.models import Noticia, Categoria
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import userRegisterForm

def noticias(request):
    nombreCategoria = 'Noticias'
    posts = Noticia.objects.filter(activo=True)
    return render(request,'noticias.html', {'posts':posts, 'nombreCategoria':nombreCategoria})

def cursos(request):
    nombreCategoria = 'Cursos'
    posts = Noticia.objects.filter(activo=True, categoria = Categoria.objects.get(nombre = 'Cursos'))
    return render(request,'noticias.html', {'posts':posts, 'nombreCategoria':nombreCategoria})

def eventos(request):
    nombreCategoria = 'Eventos'
    posts = Noticia.objects.filter(activo=True, categoria = Categoria.objects.get(nombre = 'Eventos'))
    return render(request,'noticias.html', {'posts':posts, 'nombreCategoria':nombreCategoria})

def motivacionales(request):
    nombreCategoria = 'Motivacionales'
    posts = Noticia.objects.filter(activo=True, categoria = Categoria.objects.get(nombre = 'Motivacionales'))
    return render(request,'noticias.html', {'posts':posts, 'nombreCategoria':nombreCategoria})

def galeria(request):
    nombreCategoria = 'Galería'
    posts = Noticia.objects.filter(activo=True, categoria = Categoria.objects.get(nombre = 'Galería'))
    return render(request,'noticias.html', {'posts':posts, 'nombreCategoria':nombreCategoria})

def post_detail(request, pk):
    post = get_object_or_404(Noticia, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def index(request):
    return render(request, 'index.html')

