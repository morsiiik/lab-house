from django.urls import path

from .views import *

urlpatterns = [
	path('<int:lab_number>/', lab),  # http://127.0.0.1:8000/labs/
	path('all/', la, name = 'all'),
	path('labs-available/', la, name = 'labs_av'),
	path('', main, name = 'home'),
	path('redirect/', redir)
]
