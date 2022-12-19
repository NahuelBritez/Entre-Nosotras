from django.shortcuts import render,redirect
from apps.noticia.models import Noticia
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import userRegisterForm

class NoticiaListview(ListView):
    model = Noticia
    template_name = 'index.html'

def noticias(request):
    return render(request,'noticias.html')

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