from django.urls import path

from .views import *

urlpatterns = [
    path('labs/<int:lab_number>/', lab_num),  # http://127.0.0.1:8000/labs/
    path('hello/', hello),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('redirect/', redir)
]
