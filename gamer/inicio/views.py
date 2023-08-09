from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

#solicitudes de inicio de sesion
def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'accounts/register.html',{'error':'¡Este nombre de usuario ya está tomado!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
            else:
                return render (request,'accounts/register.html',{'error':'Las contraseñas no coinciden'})
        else:
            return render(request,'acounts/register.html') 
        
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
  return render(request,"home.html")