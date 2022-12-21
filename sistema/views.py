from django.shortcuts import render,redirect
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

def registrarse(request):
    if request.method == 'POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request,f'Usuario {username} creado exitosamente.')
            return redirect(index)
    else:
        form = userRegisterForm()
    context = {'form' : form}
    return render(request,'registrarse.html',context)

def ingresar(request):
    return render(request,'ingresar.html')

def index(request):
    return render(request, 'index.html')
