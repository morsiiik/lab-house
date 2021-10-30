from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse('<h1>Articles app page</h1>')


def hot_articles(request):
	return HttpResponse('<h1>This page contains hot articles</h1>')


def classical_articles(request):
	return HttpResponse('<h1>This page contains classical articles</h1>')


def all_articles(request):
	return HttpResponse('<h1>This page contains all articles</h1>')


def main_page(request):
	return HttpResponse('<h1>This is the main page of the site\n\n\nWelcome to lab-house</h1>')
