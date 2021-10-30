from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
	return HttpResponse('<h1>Articles app page</h1>')


def hot_articles(request):
	return HttpResponse('<h1>This page contains hot articles</h1>')


def classical_articles(request):
	return HttpResponse('<h1>This page contains classical articles</h1>')


def categories(request, catid):
	if catid > 50:
		return redirect('/', permanent = False)
	return HttpResponse(f'<h1>This page contains categories</h1><p>{catid}</p>')


def all_articles(request):
	return HttpResponse('<h1>This page contains all articles</h1>')


def articles_archive(request, year):
	return HttpResponse(f'<h1>Archive by years</h1><p>{year}</p>')


def main_page(request):
	return HttpResponse('<h1>This is the main page of the site\n\n\nWelcome to lab-house</h1>')


def page_not_found(request, exception):
	return HttpResponseNotFound('<h1>It seems like there is not any page with address given</h1>')
