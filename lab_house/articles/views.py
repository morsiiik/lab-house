from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *


menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


# functions to show various pages here
def index(request):
	posts = Articles.objects.all()
	return render(request, 'articles/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
	return render(request, 'articles/about.html', {'menu': menu, 'title': 'О сайте'})


def hot_articles(request):
	return HttpResponse('<h1>This page contains hot articles</h1>')


def classical_articles(request):
	return HttpResponse('<h1>This page contains classical articles</h1>')


# get parameter treated here
def categories(request, cat_id):
	if cat_id > 50:
		return redirect('/', permanent = False)
	return HttpResponse(f'<h1>This page contains categories</h1><p>{cat_id}</p>')


def all_articles(request):
	return HttpResponse('<h1>This page contains all articles</h1>')


def articles_archive(request, year):
	return HttpResponse(f'<h1>Archive by years</h1><p>{year}</p>')


def main_page(request):
	return HttpResponse('<h1>This is the main page of the site\n\n\nWelcome to lab-house</h1>')


# function to handle 404 errors
def page_not_found(request, exception):
	return HttpResponseNotFound('<h1>It seems like there is not any page with address given</h1>')
