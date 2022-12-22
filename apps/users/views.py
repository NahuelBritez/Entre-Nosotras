from django.shortcuts import render
from django.views import generic
from .forms import RegistroUsuarioForm
from django.urls import reverse_lazy

# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')