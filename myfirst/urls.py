from django.contrib import admin
from django.urls import path, include
from articles.views import *

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', main_page),
	path('articles/', include('articles.urls'))
]
