from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro), # chama a função cadastro dentro de views localhost/usuarios/cadastro
    path('', views.auth), # retorna a pagina de autenticação localhost/usuarios
    path('login/', views.login)
]
