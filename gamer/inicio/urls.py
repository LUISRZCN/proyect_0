from django.urls import path
from .views import inicio, registro, inicio_sesion, ContactListView
from django.contrib import admin

urlpatterns = [
  path("",inicio),
  path("admin/", admin.site.urls),
  path("registro/", registro, name='registro'),
  path("inicio_sesion/", inicio_sesion, name='inicio_sesion'),
  path('contacts/', ContactListView.as_view(), name='contact-list'),
]