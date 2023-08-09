from django.urls import path
from .views import inicio, registro

urlpatterns = [
  path("",inicio),
  path("registro/", registro, name='registro'),
]