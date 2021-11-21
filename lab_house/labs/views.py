from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import *

menu = [
    {'title': 'Main', 'url_name': 'home'},
    {'title': 'All labs', 'url_name': 'all'},
    {'title': 'Labs available', 'url_name': 'labs_av'},
    {'title': 'About', 'url_name': 'about'}
]


def available_labs(request):
    context = {
        'menu': menu,
        'posts': Lab.objects.filter(is_published=True),
        'title': 'All labs available'
    }
    return render(request, 'labs/index.html', context=context)


def all_labs(request):
    context = {
        'menu': menu,
        'posts': Lab.objects.all(),
        'title': 'All labs'
    }
    return render(request, 'labs/index.html', context=context)


def main(request):
    posts = Lab.objects.all()
    context = {
        'menu': menu,
        'posts': Lab.objects.all(),
        'title': 'Main page'
    }
    return render(request, 'labs/index.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'О сайте'
    }
    return render(request, 'labs/about.html', context=context)


def lab(request, lab_number):
    context = {
        'menu': menu,
        'curr_lab': get_object_or_404(Lab, pk=lab_number)
    }
    return render(request, 'labs/curr_lab.html', context=context)


def redir(request):
    return redirect('home', permanent=True)


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена<h1>")
