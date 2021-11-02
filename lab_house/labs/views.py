from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = ["About site", "Add comment", "Sign in"]

def hello(request):
    return HttpResponse("Hello")

def redir(request):
    return redirect('home', permanent=True)

def index(request):
    posts = Lab.objects.all()
    return render(request, 'labs/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'labs/about.html', {'menu': menu, 'title': 'О сайте'})

def lab_num(request, lab_number):
    return HttpResponse(f"<h1>Лаба</h1><p>{lab_number}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена<h1>")
