from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import RegistroForm
from .forms import LoginForm
#solicitudes de inicio de sesion

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Aquí puedes guardar los datos del formulario en la base de datos
            # y realizar otras acciones necesarias.
            return redirect('ruta_hacia_pagina_exitosa')  # Redirige a la página de éxito
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})


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


def inicio(request):
  data={"titulo":"GamerSpeak"}
  return render(request,"home.html",data)

