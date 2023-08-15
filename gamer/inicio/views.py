from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import RegistroForm
from .forms import LoginForm
from django.views import generic
from .models import Contact
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
#solicitudes de inicio de sesion

#codigo de registro

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Verifica si ya existe un usuario con el mismo nombre de usuario
            if User.objects.filter(username=username).exists():
                # Aquí puedes manejar el caso de un nombre de usuario ya existente
                pass
            else:
                # Crea el usuario
                username = User.objects.create_user(username=username, email=email, password=password)
                # Puedes realizar más acciones aquí si es necesario, como iniciar sesión automáticamente
                return redirect('inicio_sesion.html')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

#codigo de inicio de sesion
def inicio_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            contraseña = form.cleaned_data['contraseña']
            user = authenticate(request, username=correo, password=contraseña)
            if user is not None:
                login(request, user)
                return redirect('ruta_hacia_pagina_exitosa')  # Redirige a la página de éxito
    else:
        form = LoginForm()

    return render(request, 'inicio_sesion.html', {'form': form})

#render del titulo
def inicio(request):
  data={"titulo":"GamerSpeak"}
  return render(request,"home.html",data)


class ContactListView(LoginRequiredMixin, generic.ListView):
    model = Contact
    context_object_name = 'contact_list'   # su propio nombre para la lista como variable de plantilla
    template_name = 'contact_list.html'  # Especifique su propio nombre/ubicación de plantilla


