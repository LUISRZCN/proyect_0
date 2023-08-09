from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
      nombre = forms.CharField(max_length=30)
      correo = forms.EmailField(max_length=200)
      apodo = forms.CharField(max_length=30)

      class Meta:
        model = User
        fields = ('username', 'nombre', 'correo', 'apodo', 'password1', 'password2', )