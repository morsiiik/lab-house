from django.urls import path
from .views import *

urlpatterns = [
	path('hot/', hot_articles),
	path('all/', all_articles),
	path('classical/', classical_articles),
]
