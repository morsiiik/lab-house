from django.urls import path, re_path  # for regular expressions
from .views import * # imports all the function in the concerned file

urlpatterns = [
	path('', index, name = 'home'),  # home path, redirection also if 'home' returned with redirection somewhere
	path('hot/', hot_articles),  # to hot
	path('all/', all_articles),  # to all
	path('classical/', classical_articles),  # to classical articles
	path('categories/<int:cat_id>', categories),  # to categories with get parameter
	re_path(r'^archive/(?P<year>[0-9]{4})/', articles_archive),  # to archive with template parameters
]
