from django.db import models
from django.contrib.auth.models import AbstractUser

#class Usuarios(AbstractUser):
 #   nombre = models.CharField(max_length=100)
  #  apodo = models.CharField(max_length=50)
   # email = models.EmailField(unique=True)
    #contraseña = models.CharField(max_length=128)
    #confirmacion_contraseña = models.CharField(max_length=128)  # Para confirmar la contraseña

    #def __str__(self):
     #   return self.username


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)

    def __str__(self):
        return self.name