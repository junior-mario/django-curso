from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def cadastro(request):
    return render(request, 'cadastro/index.html')

def auth(request):
    return HttpResponse('Pagina de autenticação')

def login(request):
    return HttpResponse('Pagina de login')
