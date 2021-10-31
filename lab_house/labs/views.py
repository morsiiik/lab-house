from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello")


def lab_num(request, lab_number):
    return HttpResponse(f"<h1>Лаба</h1><p>{lab_number}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена<h1>")
