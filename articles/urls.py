from django.urls import path, re_path # for regular expressions
from .views import *

urlpatterns = [
	path('hot/', hot_articles),
	path('all/', all_articles),
	path('classical/', classical_articles),
	re_path(r'^archive/(?P<year>[0-9]{4})/', articles_archive),
]
