from django.urls import path
from .views import inicio, registro, inicio_sesion

urlpatterns = [
  path("",inicio),
  path("registro/", registro, name='registro'),
  path("inicio_sesion/", inicio_sesion, name='inicio_sesion'),
]