from django import forms


class RegistroForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    apodo = forms.CharField(label='Apodo', max_length=50)
    email = forms.EmailField(label='Correo electrónico')
    contraseña = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    confirmacion_contraseña = forms.CharField(label='Confirmación de contraseña', widget=forms.PasswordInput)


class LoginForm(forms.Form):
    correo = forms.EmailField(label='Correo electrónico')
    contraseña = forms.CharField(label='Contraseña', widget=forms.PasswordInput)