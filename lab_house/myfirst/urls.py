from django.contrib import admin
from django.urls import path, include
from articles.views import *

urlpatterns = [
	path('', main_page),
	path('admin/', admin.site.urls),
	path('articles/', include('articles.urls'))
]

handler404 = page_not_found
