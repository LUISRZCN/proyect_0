from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import RegistroForm

#solicitudes de inicio de sesion

def registro(request):
       if request.method == 'POST':
           form = RegistroForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('login')
       else:
           form = RegistroForm()

       return render(request, 'registro.html', {'form': form})

        
def login(request):
        if request.method == 'POST':
            user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
            if user is not None:
                auth.login(request,user)
                return redirect('home')
            else:
                return render (request,'accounts/login.html',{'error','¡Nombre de usuario o contraseña incorrecta!'})
        else:
            return render(request,'accounts/login.html')

def logout(request):
        if request.method == 'POST':
            auth.logout(request)
        return redirect('home')

def inicio(request):
  data={"titulo":"Inicio"}
  return render(request,"home.html",data)

