from django.urls import path

from .views import *

urlpatterns = [
    path('lab/<int:lab_number>/', lab),  # http://127.0.0.1:8000/labs/
    path('all/', all_labs, name='all'),
    path('labs-available/', available_labs, name='labs_av'),
    path('', main, name='home'),
    path('about/', about, name='about'),
    path('redirect/', redir)

]
