from django.urls import path
from . import views

urlpatterns = [
    path("", views.hola, name="Hola"),
    path("", views.saludo, name="El_Saludo"),
]
