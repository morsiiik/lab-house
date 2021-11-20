from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [
	{'title': 'Main', 'url_name': 'home'},
	{'title': 'All labs', 'url_name': 'all'},
	{'title': 'Labs available', 'url_name': 'labs_av'},
]


def la(request):
	context = {
		'menu': menu,
		'posts': Lab.objects.all(),
		'title': 'All labs available'
	}
	return render(request, 'labs/index.html', context = context)


def redir(request):
	return redirect('home', permanent = True)


def main(request):
	posts = Lab.objects.all()
	return render(request, 'labs/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
	return render(request, 'labs/about.html', {'menu': menu, 'title': 'О сайте'})


def lab(request, lab_number):
	return HttpResponse(f"<h1>Лаба</h1><p>{lab_number}</p>")


def page_not_found(request, exception):
	return HttpResponseNotFound(f"<h1>Страница не найдена<h1>")
